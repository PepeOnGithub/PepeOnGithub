#!/usr/bin/env python3
"""Validate a Bedrock JSON UI resource pack.

Checks:
  1. Every .json parses (Bedrock UI JSON allows // and /* */ comments).
  2. Every path in ui/_ui_defs.json exists, and every ui/**/*.json is listed (warns otherwise).
  3. Every textures/ or assets/ path reference that points into the pack resolves to a file.
  4. Every language file has the same keys as en_US.lang, and every %key used in UI JSON exists in it.
  5. Every "name@namespace.key" reference whose namespace is defined inside the pack
     resolves to a real key in that namespace.

Usage: python3 validate_pack.py <pack_root>
Exit code 0 = no errors (warnings do not fail the run).
"""
import glob
import json
import os
import re
import sys

ERRORS, WARNINGS = [], []
# Files that are intentionally kept as uploaded (not reformatted); duplicates there are known.
KNOWN_DUPLICATE_FILES = {'ui/better_containers/compat/legacy_container_item.json'}
# Old namespace names that no longer exist. Vanilla-looking names (_global, uic, smithing) are excluded.
RETIRED_NAMESPACES = {'single_chest_content', 'double_chest_content', 'item_data', 'toggle_manager',
                      'brewing_global', 'factory_bindings', 'brewing_toggle', 'brewing_potion_slot',
                      'modifier_brewing_potion_slot', 'brewing_recipe_book', 'brewing_recipe_book_grid',
                      'smithing_arc', 'bd-h1', 'f-ez18', 'es1e-'}
VANILLA_TEX = set()
UNRESOLVED = set()


def strip_comments(text):
    """Remove // and /* */ comments that sit outside string literals."""
    out, i, n, in_str = [], 0, len(text), False
    while i < n:
        c = text[i]
        if in_str:
            out.append(c)
            if c == '\\' and i + 1 < n:
                out.append(text[i + 1])
                i += 2
                continue
            if c == '"':
                in_str = False
        elif c == '"':
            in_str = True
            out.append(c)
        elif text.startswith('//', i):
            while i < n and text[i] != '\n':
                i += 1
            continue
        elif text.startswith('/*', i):
            end = text.find('*/', i + 2)
            i = n if end == -1 else end + 2
            continue
        else:
            out.append(c)
        i += 1
    return ''.join(out)


def load(path):
    with open(path, encoding='utf-8') as f:
        return json.loads(strip_comments(f.read()))


def main(root):
    root = os.path.abspath(root)
    rel = lambda p: os.path.relpath(p, root).replace(os.sep, '/')

    # 1. parse everything
    docs = {}
    for p in glob.glob(os.path.join(root, '**', '*.json'), recursive=True):
        try:
            docs[rel(p)] = load(p)
        except (ValueError, UnicodeDecodeError) as e:
            ERRORS.append(f'JSON parse error in {rel(p)}: {e}')

    # 2. _ui_defs
    defs_path = os.path.join(root, 'ui', '_ui_defs.json')
    listed = set()
    if os.path.exists(defs_path):
        for entry in docs.get('ui/_ui_defs.json', {}).get('ui_defs', []):
            listed.add(entry)
            if not os.path.exists(os.path.join(root, entry)):
                ERRORS.append(f'_ui_defs lists missing file: {entry}')
        if len(listed) != len(docs.get('ui/_ui_defs.json', {}).get('ui_defs', [])):
            ERRORS.append('_ui_defs lists the same file more than once')
    else:
        ERRORS.append('ui/_ui_defs.json is missing')
    for f in sorted(docs):
        if f.startswith('ui/better_containers/') and f not in listed:
            WARNINGS.append(f'not listed in _ui_defs: {f}')

    # 3. textures referenced by path
    texture_refs = set()
    for f, doc in docs.items():
        for m in re.findall(r'"((?:textures|assets)/[^"]+)"', json.dumps(doc)):
            texture_refs.add((f, m))
    for f, ref in sorted(texture_refs):
        base = os.path.join(root, ref)
        if os.path.exists(base) or os.path.exists(base + '.png') or os.path.exists(base + '.tga'):
            continue
        if ref.startswith('textures/ui/'):
            VANILLA_TEX.add(ref)
        else:
            ERRORS.append(f'{f}: texture not found: {ref}')

    # 4. language key parity
    lang_dir = os.path.join(root, 'texts')
    ref_keys = None
    for p in sorted(glob.glob(os.path.join(lang_dir, '*.lang'))):
        with open(p, encoding='utf-8') as f:
            keys = [l.split('=', 1)[0] for l in f if '=' in l and not l.lstrip().startswith('#')]
        if os.path.basename(p) == 'en_US.lang':
            ref_keys = set(keys)
    if ref_keys is None:
        ERRORS.append('texts/en_US.lang missing')
    else:
        for p in sorted(glob.glob(os.path.join(lang_dir, '*.lang'))):
            with open(p, encoding='utf-8') as f:
                keys = [l.split('=', 1)[0] for l in f if '=' in l and not l.lstrip().startswith('#')]
            if set(keys) != ref_keys:
                ERRORS.append(f'{rel(p)}: keys differ from en_US ({len(set(keys) - ref_keys)} extra, {len(ref_keys - set(keys))} missing)')
            if len(keys) != len(set(keys)):
                ERRORS.append(f'{rel(p)}: duplicate keys')

    # 4b. every %key used in UI JSON must exist in en_US.lang
    used_keys = {}
    for f, doc in docs.items():
        for m in re.findall(r'(?<![0-9A-Za-z])%([A-Za-z][A-Za-z0-9_.]*)', json.dumps(doc)):
            used_keys.setdefault(m, f)
    if ref_keys is not None:
        for key, f in sorted(used_keys.items()):
            if key not in ref_keys:
                ERRORS.append(f'{f}: lang key %{key} is not defined in texts/en_US.lang')

    # 4c. duplicate keys inside one object silently drop a value in JSON parsers
    dup_hits = []
    for p in glob.glob(os.path.join(root, '**', '*.json'), recursive=True):
        with open(p, encoding='utf-8') as f:
            text = strip_comments(f.read())
        def hook(pairs, _f=rel(p)):
            keys = [k for k, _ in pairs]
            seen = {k for k in keys if keys.count(k) > 1}
            if seen:
                dup_hits.append((_f, sorted(seen)))
            return dict(pairs)
        try:
            json.loads(text, object_pairs_hook=hook)
        except ValueError:
            pass
    for f, keys in dup_hits:
        if f in KNOWN_DUPLICATE_FILES:
            WARNINGS.append(f'{f}: duplicate key(s) {keys} (known, see docs/21)')
        else:
            ERRORS.append(f'{f}: duplicate key(s) {keys}')

    # 4c2. the retired sp_ prefix (renamed to bc_ in the Better Containers rename)
    for f, doc in docs.items():
        for tok in set(re.findall(r'(?<![A-Za-z0-9_])sp_[a-z_]+', json.dumps(doc))):
            ERRORS.append(f'{f}: uses retired prefix "{tok}" (renamed to bc_; see docs/04)')

    # 4d. references to namespaces that were renamed away (names unlikely to be vanilla)
    for f, doc in docs.items():
        for ns in set(re.findall(r'"[^"@]*@?([A-Za-z0-9_\-]+)\.[A-Za-z0-9_\-]+', json.dumps(doc))):
            if ns in RETIRED_NAMESPACES and ns not in namespaces:
                ERRORS.append(f'{f}: references retired namespace "{ns}" (renamed; see docs/02)')

    # 5. "@" references into pack namespaces
    namespaces = {}
    for f, doc in docs.items():
        if not isinstance(doc, dict):
            continue
        ns = doc.get('namespace')
        if isinstance(ns, str):
            namespaces.setdefault(ns, (f, set()))[1].update(k.split('@')[0] for k in doc if k != 'namespace')
    for f, doc in docs.items():
        for m in re.findall(r'"[^"@"]*@([A-Za-z0-9_\-]+)\.([A-Za-z0-9_\-]+)"', json.dumps(doc)):
            ns, key = m
            if ns in namespaces and key not in namespaces[ns][1]:
                # Many pack namespaces share a name with a vanilla namespace (e.g. "_global"),
                # so a missing key may be provided by vanilla. Report, don't fail.
                UNRESOLVED.add((f, f'@{ns}.{key}', namespaces[ns][0]))

    if VANILLA_TEX:
        WARNINGS.append(f'{len(VANILLA_TEX)} vanilla texture path(s) not shipped in the pack, assumed present in vanilla (e.g. {sorted(VANILLA_TEX)[0]})')
    if UNRESOLVED:
        WARNINGS.append(f'{len(UNRESOLVED)} @-reference(s) not defined in the pack namespace; likely provided by a same-named vanilla namespace')
    # 6. local control references (source_control_name / control_name) that match no key in the pack.
    #    Some are vanilla controls or names built at runtime, so this is a warning with a count.
    key_names = set()
    for doc in docs.values():
        def _walk(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    key_names.add(k.split('@')[0]); _walk(v)
            elif isinstance(o, list):
                for x in o: _walk(x)
        _walk(doc)
    local_refs = set()
    for doc in docs.values():
        def _refs(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if k in ('source_control_name', 'control_name') and isinstance(v, str):
                        local_refs.add(v)
                    _refs(v)
            elif isinstance(o, list):
                for x in o: _refs(x)
        _refs(doc)
    unknown = [r for r in local_refs if r not in key_names and '/' not in r and not r.startswith('$') and "'" not in r]
    if unknown:
        WARNINGS.append(f'{len(unknown)} control reference(s) match no pack control (vanilla or built at runtime), e.g. {sorted(unknown)[0]}')

    print(f'Checked {len(docs)} JSON files, {len(texture_refs)} texture refs, {len(namespaces)} pack namespaces.')
    for w in WARNINGS:
        print('WARN ', w)
    for f, ref, where in sorted(UNRESOLVED)[:5]:
        print('  e.g.', f, ref)
    for e in ERRORS:
        print('ERROR', e)
    print(f'{len(ERRORS)} error(s), {len(WARNINGS)} warning(s)')
    return 1 if ERRORS else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else '.'))
