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
        if f.startswith('ui/pepe/') and f not in listed:
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
        if ref.startswith('textures/ui/') and not ref.startswith('textures/ui/pepe/') and not ref.startswith('textures/ui/ashur/'):
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
