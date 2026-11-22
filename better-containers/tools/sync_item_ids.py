#!/usr/bin/env python3
"""Check and update item ID variables in pack/ui/_global_variables.json.

Source: an item list in the format used by the Minecraft Item ID Viewer
(https://github.com/AsakiYuki/minecraft-item-id-viewer), which returns
{"version": ..., "items": [{"name": "minecraft:<id>", "id": N, "id_aux": N*65536}, ...]}.
The list for the current stable version is saved in data/item_ids/.

Usage:
  python3 tools/sync_item_ids.py                       # report only
  python3 tools/sync_item_ids.py --write               # also apply corrections
  python3 tools/sync_item_ids.py --list data/item_ids/other.json

Only variables named $<item>_item_id (plus the explicit ALIAS table) are checked.
Brewing potion values ($bc_brewing:potion_of_*) are potion types, not items, so they are not checked.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
VARS = os.path.join(ROOT, 'pack', 'ui', '_global_variables.json')
DEFAULT_LIST = os.path.join(ROOT, 'data', 'item_ids', 'stable-1.26.60.json')

# variable base name -> item name in the list, where they differ
ALIAS = {
    'turtle_shell': 'turtle_helmet',
    'redstone_dust': 'redstone',
    'nether_quartz': 'quartz',
    'netherite_upgrade': 'netherite_upgrade_smithing_template',
    'glistering_melon': 'glistering_melon_slice',
    'dragons_breath': 'dragon_breath',
    'cobweb': 'web',
    'slime_block': 'slime',
    # UI tab and button icons: the pack shows a vanilla item as the icon (checked in data/item_ids)
    'armor_items_tab': 'iron_chestplate',
    'armor_preview_button': 'diamond_chestplate',
    'mineral_items_tab': 'quartz',
    'smithing_template_tab': 'netherite_upgrade_smithing_template',
    # not an item: a brewing recipe state
    'awkward_potion': None,
}
# variable base names that are UI tab/button icons, not the item itself. Their IDs are checked as well.
TRIM_SUFFIX = '_trim'


def item_name_for(var):
    base = var[1:]
    base = re.sub(r'^bc_brewing:', '', base)
    base = re.sub(r'_item_id$', '', base)
    if base in ALIAS:
        return ALIAS[base]
    if base.endswith(TRIM_SUFFIX):
        return base[: -len(TRIM_SUFFIX)] + '_armor_trim_smithing_template'
    return ALIAS.get(base, base)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--list', default=DEFAULT_LIST)
    ap.add_argument('--write', action='store_true')
    args = ap.parse_args()

    listing = json.load(open(args.list, encoding='utf-8'))
    by_name = {i['name'].split(':', 1)[1]: i['id'] for i in listing['items']}
    variables = json.load(open(VARS, encoding='utf-8'))

    ok, fixed, unknown = 0, [], []
    for key, value in variables.items():
        if key.startswith('$bc_brewing:potion_of_'):
            continue
        if not (re.match(r'^\$[a-z_:]+_item_id$', key) or key.startswith('$bc_brewing:')):
            continue
        name = item_name_for(key)
        if name is None:
            continue
        if name not in by_name:
            unknown.append((key, value, name))
            continue
        if by_name[name] == value:
            ok += 1
        else:
            fixed.append((key, value, by_name[name]))
            if args.write:
                variables[key] = by_name[name]

    print(f"list: {listing['version']} ({len(listing['items'])} items)")
    print(f"matching: {ok}")
    for key, old, new in fixed:
        print(f"CORRECT {key}: {old} -> {new}")
    for key, value, name in unknown:
        print(f"not in list, left unchanged: {key} = {value} (looked for '{name}')")
    if args.write and fixed:
        with open(VARS, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(variables, f, indent=2, ensure_ascii=False)
            f.write('\n')
        print(f"wrote {len(fixed)} correction(s) to {os.path.relpath(VARS, ROOT)}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
