#!/usr/bin/env python3
"""Generate the in-game furnace guide panel (furnace, blast furnace, smoker).

Writes:
  pack/ui/better_containers/shared/item_cell.json          (shared item cell template)
  pack/ui/better_containers/containers/furnace_guide.json  (namespace bc_furnace_guide)
  pack/ui/_global_variables.json                           ($<item>_item_id entries, added if missing)
  pack/texts/*.lang                                        (guide strings, added to every locale)
  pack/ui/furnace_screen.json                              (adds the guide to the furnace screen)

Item IDs come from data/item_ids/stable-1.26.60.json. Run tools/sync_item_ids.py to check them.
Re-run this script after changing the tab lists below. It is safe to run again.
"""
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACK = os.path.join(ROOT, 'pack')
LIST = os.path.join(ROOT, 'data', 'item_ids', 'stable-1.26.60.json')
COLUMNS = 8          # item cells per row (8 x 18px = 144px)
CELL = 18

# Tabs of the furnace guide. Items are vanilla item names (no namespace) from the item list.
# Curated: only real furnace inputs, smoker inputs, or fuel. See docs/guides/01-furnace.md.
TABS = [
    ('foods', 'Foods', ['beef', 'porkchop', 'chicken', 'mutton', 'rabbit', 'cod', 'salmon', 'potato', 'kelp']),
    ('ores', 'Ores', ['coal_ore', 'copper_ore', 'diamond_ore', 'emerald_ore', 'gold_ore', 'iron_ore', 'lapis_ore',
                      'nether_gold_ore', 'quartz_ore', 'redstone_ore', 'ancient_debris', 'raw_copper', 'raw_gold', 'raw_iron']),
    ('blocks', 'Blocks', ['cobblestone', 'sand', 'clay', 'netherrack', 'basalt', 'cobbled_deepslate',
                          'stone_bricks', 'deepslate_bricks', 'deepslate_tiles']),
    ('nature', 'Nature', ['cactus', 'chorus_fruit', 'sea_pickle', 'clay_ball', 'oak_log']),
    ('fuel', 'Fuel', ['coal', 'charcoal', 'coal_block', 'blaze_rod', 'lava_bucket', 'dried_kelp_block', 'bamboo',
                      'bamboo_block', 'stick']),
]
# Which screens hide a tab (vanilla variables). Foods label hidden on blast furnace, ores on smoker.
HIDDEN_ON = {'foods': '$is_blast_furnace', 'ores': '$is_smoker'}


def load_items():
    data = json.load(open(LIST, encoding='utf-8'))
    return {i['name'].split(':', 1)[1]: i['id'] for i in data['items']}


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')


def item_cell_file():
    return {
        'namespace': 'bc_item_cell',
        'item_cell': {
            'type': 'panel',
            'size': [CELL, CELL],
            '$item_id|default': 0,
            '$item_id_aux|default': 0,
            'controls': [{
                'icon@common.item_renderer': {
                    'size': [CELL - 2, CELL - 2],
                    'anchor_from': 'center',
                    'anchor_to': 'center',
                    'property_bag': {
                        '#item_id': '($item_id * 65536)',
                        '#full_item_id': '$item_id_aux',
                    },
                    'bindings': [{
                        'binding_type': 'view',
                        'source_property_name': '(#full_item_id + #item_id)',
                        'target_property_name': '#item_id_aux',
                    }],
                }
            }],
        },
    }


def tab_toggle_name(key):
    return f'{key}_tab_toggle'


def tab_panel(key, items):
    rows = []
    for start in range(0, len(items), COLUMNS):
        chunk = items[start:start + COLUMNS]
        cells = {f'{name}_cell@bc_item_cell.item_cell': {'$item_id': f'${name}_item_id'} for name in chunk}
        rows.append({f'row_{start // COLUMNS}': {
            'type': 'stack_panel',
            'orientation': 'horizontal',
            'size': ['100%', CELL],
            'controls': [{k: v} for k, v in cells.items()],
        }})
    panel = {
        'type': 'stack_panel',
        'orientation': 'vertical',
        'size': ['100%', 'default'],
        'controls': [{k: v} for row in rows for k, v in row.items()],
        'bindings': [{
            'binding_type': 'view',
            'source_control_name': tab_toggle_name(key),
            'source_property_name': '#toggle_state',
            'target_property_name': '#visible',
        }],
    }
    if key in HIDDEN_ON:
        panel['ignored'] = HIDDEN_ON[key]
    return panel


def guide_file(ids):
    tabs = []
    labels = {}
    for index, (key, title, _) in enumerate(TABS):
        label = f'{key}_label'
        labels[f'{label}@bc_furnace_guide.tab_label'] = {'$tab_text': f'%bc_furnace_guide.tab.{key}'}
        tab = {
            'type': 'panel',
            'size': [28, 14],
            'controls': [{f'{key}_tab@bc_shared.radio': {
                '$toggle_name': 'furnace_guide_tabs',
                '$toggle_view_binding_name': tab_toggle_name(key),
                '$toggle_group_forced_index': index,
                '$toggle_default_state': key == 'foods',
                '$button_content': f'bc_furnace_guide.{label}',
                'size': [28, 14],
            }}],
        }
        if key in HIDDEN_ON:
            tab['ignored'] = HIDDEN_ON[key]
        tabs.append({f'{key}_tab_slot': tab})
    panels = [{f'{key}_panel': tab_panel(key, items)} for key, _, items in TABS]
    out = {
        'namespace': 'bc_furnace_guide',
        'tab_label': {
            'type': 'label',
            'text': '$tab_text',
            'size': ['100%', 12],
            'font_size': 'small',
        },
        'furnace_guide': {
            'type': 'panel',
            'size': [CELL * COLUMNS, 'default'],
            '$is_blast_furnace|default': False,
            '$is_smoker|default': False,
            'layer': 2,
            'controls': [
                {'title_label': {
                    'type': 'label',
                    'text': '%bc_furnace_guide.title',
                    'size': ['100%', 12],
                }},
                {'tab_bar': {
                    'type': 'stack_panel',
                    'orientation': 'horizontal',
                    'size': ['100%', 16],
                    'controls': [{k: v} for t in tabs for k, v in t.items()],
                }},
                {'tab_contents': {
                    'type': 'panel',
                    'size': ['100%', 'default'],
                    'controls': [{k: v} for p in panels for k, v in p.items()],
                }},
            ],
        },
    }
    out.update(labels)
    return out


def hook_file():
    return {
        'modifications': [{
            'array_name': 'controls',
            'operation': 'insert_back',
            'value': {'furnace_guide@bc_furnace_guide.furnace_guide': {}},
        }]
    }


def main():
    items = load_items()
    all_names = [n for _, _, names in TABS for n in names]
    missing = [n for n in all_names if n not in items]
    if missing:
        raise SystemExit(f'not in item list: {missing}')
    ids = {n: items[n] for n in all_names}

    # shared item cell
    write(os.path.join(PACK, 'ui/better_containers/shared/item_cell.json'), item_cell_file())

    # the guide itself
    write(os.path.join(PACK, 'ui/better_containers/containers/furnace_guide.json'), guide_file(ids))

    # variables: one $<name>_item_id per item, added only if missing (never overwrite)
    vpath = os.path.join(PACK, 'ui/_global_variables.json')
    variables = json.load(open(vpath, encoding='utf-8'))
    added = 0
    for n in all_names:
        key = f'${n}_item_id'
        if key not in variables:
            variables[key] = ids[n]
            added += 1
        elif variables[key] != ids[n]:
            raise SystemExit(f'{key} already exists with {variables[key]}, expected {ids[n]}; resolve by hand')
    write(vpath, variables)
    print('variables added:', added)

    # the vanilla furnace screen: append the guide after the management row
    hpath = os.path.join(PACK, 'ui/furnace_screen.json')
    hook = json.load(open(hpath, encoding='utf-8'))
    key = 'right_panel/furnace_screen_inventory'
    mods = hook[key]['modifications']
    if not any('furnace_guide@' in json.dumps(m) for m in mods):
        mods.append(hook_file()['modifications'][0])
    write(hpath, hook)

    # register the new UI files so the game loads them
    dpath = os.path.join(PACK, 'ui/_ui_defs.json')
    defs = json.load(open(dpath, encoding='utf-8'))['ui_defs']
    for entry in ['ui/better_containers/shared/item_cell.json',
                  'ui/better_containers/containers/furnace_guide.json']:
        if entry not in defs:
            defs.append(entry)
    write(dpath, {'ui_defs': defs})

    # translation keys, added to every locale (English text as the placeholder)
    strings = {
        'bc_furnace_guide.title': 'Furnace Guide',
        'bc_furnace_guide.tab.foods': 'Foods',
        'bc_furnace_guide.tab.ores': 'Ores',
        'bc_furnace_guide.tab.blocks': 'Blocks',
        'bc_furnace_guide.tab.nature': 'Nature',
        'bc_furnace_guide.tab.fuel': 'Fuel',
    }
    for path in sorted(glob.glob(os.path.join(PACK, 'texts', '*.lang'))):
        lines = open(path, encoding='utf-8').read().split('\n')
        existing = {l.split('=', 1)[0] for l in lines if '=' in l and not l.lstrip().startswith('#')}
        new = [f'{k}={v}' for k, v in strings.items() if k not in existing]
        if new:
            text = '\n'.join(lines).rstrip('\n') + '\n' + '\n'.join(new) + '\n'
            open(path, 'w', encoding='utf-8', newline='\n').write(text)
    print('lang keys added to', len(glob.glob(os.path.join(PACK, 'texts', '*.lang'))), 'files')


if __name__ == '__main__':
    main()
