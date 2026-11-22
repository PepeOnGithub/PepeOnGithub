#!/usr/bin/env python3
"""Apply data/translations/<locale>.json (long guide text) onto pack/texts/<locale>.lang.

Usage: apply_translations.py [SOURCE_DIR]
With SOURCE_DIR, each <locale>.json is first checked and copied into
data/translations/. A file is rejected if its keys differ from the English
source or it changes the section-sign codes of a string.
"""
import glob, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, 'data', 'translations')


def english_long_text():
    import translate_ui_labels as t
    short = set(t.KEYS)
    out = {}
    for line in open(os.path.join(ROOT, 'pack', 'texts', 'en_US.lang'), encoding='utf-8'):
        line = line.rstrip('\n')
        if line.startswith('bc_') and '=' in line:
            k, v = line.split('=', 1)
            if k not in short:
                out[k] = v
    return out


def codes(s):
    return re.findall(r'§.', s)


def check(loc, data, en, full=True):
    problems = []
    if full and set(data) != set(en):
        problems.append(f'key mismatch: {len(set(en) - set(data))} missing, {len(set(data) - set(en))} extra')
    for k, v in data.items():
        if k in en:
            if not isinstance(v, str) or not v.strip():
                problems.append(f'{k}: empty')
            elif codes(v) != codes(en[k]):
                problems.append(f'{k}: § codes changed')
            elif '\n' in v:
                problems.append(f'{k}: newline')
    return problems


def main():
    en = english_long_text()
    os.makedirs(STORE, exist_ok=True)
    if len(sys.argv) > 1:
        for path in sorted(glob.glob(os.path.join(sys.argv[1], '*.json'))):
            loc = os.path.basename(path)[:-5]
            if loc == 'source_en':
                continue
            data = json.load(open(path, encoding='utf-8'))
            probs = check(loc, data, en)
            if probs:
                print('REJECT', loc, probs[:3])
            else:
                shutil.copy(path, os.path.join(STORE, loc + '.json'))
    applied = 0
    for path in sorted(glob.glob(os.path.join(STORE, '*.json'))):
        loc = os.path.basename(path)[:-5]
        data = json.load(open(path, encoding='utf-8'))
        data = {k: v for k, v in data.items() if k in en and not check(loc, {k: v}, {k: en[k]}, full=False)}
        # keys added or changed in English after the translation stay English
        lang = os.path.join(ROOT, 'pack', 'texts', loc + '.lang')
        text = open(lang, encoding='utf-8').read()
        for k, v in data.items():
            text, n = re.subn(rf'^{re.escape(k)}=.*$', lambda m: f'{k}={v}', text, flags=re.M)
            if not n:
                text = text.rstrip('\n') + f'\n{k}={v}\n'
        open(lang, 'w', encoding='utf-8').write(text)
        applied += 1
    print('applied long text for', applied, 'locales')


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
