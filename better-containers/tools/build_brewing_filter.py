#!/usr/bin/env python3
"""Wire the brewing recipe-book polarity filter (All / Positive / Negative / Mixed).

Each potion in the recipe grid is a fixed control with a known potion key, so
its polarity is looked up in data/potion_polarity.json and written onto the
control as $polarity_control. A row of four radio toggles shows or hides the
grid items. Safe to re-run.
"""
import glob, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BREW = os.path.join(ROOT, 'pack', 'ui', 'better_containers', 'brewing', 'recipe_book')
FILTERS = [('all', 'All'), ('positive', 'Good'), ('negative', 'Bad'), ('mixed', 'Mixed')]
LABEL_KEY = 'bc_brewing_filter.{}'


def load(p):
    return json.load(open(p, encoding='utf-8'))


def save(p, d):
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write('\n')


def polarity_map():
    pol = load(os.path.join(ROOT, 'data', 'potion_polarity.json'))
    out = {}
    for kind in ('positive', 'negative', 'mixed'):
        for name in pol[kind]:
            out[name] = kind
    return out


def filter_toggle(index, key):
    return {
        f'bc_filter_{key}': {
            'type': 'toggle',
            'size': [34, 15],
            'toggle_name': 'bc_brewing_filter',
            'radio_toggle_group': True,
            'toggle_default_state': index == 0,
            'toggle_group_forced_index': index,
            'toggle_group_default_selected': 0,
            'property_bag': {'#toggle_state': index == 0},
            'sound_name': 'random.click',
            'button_mappings': [
                {'from_button_id': 'button.menu_select', 'to_button_id': 'button.menu_ok', 'mapping_type': 'pressed'},
                {'from_button_id': 'button.menu_ok', 'to_button_id': 'button.menu_ok', 'mapping_type': 'pressed'},
            ],
            'unchecked_control': 'bc_brewing_recipe_book.filter_off',
            'checked_control': 'bc_brewing_recipe_book.filter_on',
            'unchecked_hover_control': 'bc_brewing_recipe_book.filter_off',
            'checked_hover_control': 'bc_brewing_recipe_book.filter_on',
            'layer': 8,
            'controls': [{'filter_label': {
                'type': 'label', 'text': '%' + LABEL_KEY.format(key),
                'font_size': 'small', 'layer': 10, 'anchor_from': 'center', 'anchor_to': 'center',
                'color': '$title_text_color'}}],
        }
    }


def main():
    pol = polarity_map()
    gp = os.path.join(BREW, 'recipe_grid.json')
    grid = load(gp)
    missing = []
    for entry in grid['recipe_book_grid@bc_brewing_common.text_keys']['controls']:
        (name, props), = entry.items()
        if not name.startswith('potion_') or '$potion_key_type' not in props:
            continue
        key = re.sub(r'^is_(.*)_key$', r'\1', props['$potion_key_type'])
        kind = pol.get(key)
        if kind is None and key != 'awkward_potion':
            missing.append(key)
        props['$polarity_control'] = f'bc_filter_{kind or "all"}'
    item = grid['recipe_grid_item@bc_brewing_recipe_grid.item_toggle']
    item['$polarity_control|default'] = 'bc_filter_all'
    item['bindings'] = [
        {'binding_type': 'view', 'source_control_name': 'bc_filter_all',
         'source_property_name': '#toggle_state', 'target_property_name': '#filter_all'},
        {'binding_type': 'view', 'source_control_name': '$polarity_control',
         'source_property_name': '#toggle_state', 'target_property_name': '#filter_match'},
        {'binding_type': 'view', 'source_property_name': '(#filter_all or #filter_match)',
         'target_property_name': '#visible'},
    ]
    save(gp, grid)

    bp = os.path.join(BREW, 'recipe_book.json')
    book = load(bp)
    book['filter_on'] = {'type': 'image', 'texture': 'textures/ui/craft_toggle_on', 'size': [34, 15], 'layer': 8}
    book['filter_off'] = {'type': 'image', 'texture': 'textures/ui/craft_toggle_off', 'size': [34, 15], 'layer': 8}
    book['filter_row'] = {
        'type': 'stack_panel', 'orientation': 'horizontal', 'size': ['100%', 15],
        'anchor_from': 'bottom_left', 'anchor_to': 'bottom_left', 'offset': [4, -2], 'layer': 8,
        'controls': [filter_toggle(i, k) for i, (k, _) in enumerate(FILTERS)],
    }
    holder = find_content(book)
    holder['controls'] = [c for c in holder['controls'] if 'filter_row@bc_brewing_recipe_book.filter_row' not in c]
    holder['controls'].append({'filter_row@bc_brewing_recipe_book.filter_row': {}})
    save(bp, book)

    for lang in glob.glob(os.path.join(ROOT, 'pack', 'texts', '*.lang')):
        text = open(lang, encoding='utf-8').read()
        add = ''.join(f'{LABEL_KEY.format(k)}={v}\n' for k, v in FILTERS if LABEL_KEY.format(k) + '=' not in text)
        if add:
            open(lang, 'w', encoding='utf-8').write(text.rstrip('\n') + '\n' + add)
    print('filter wired; unclassified potions:', missing or 'none')


def find_content(node):
    if isinstance(node, dict):
        if 'recipe_book_content@bc_brewing_common.root_panel' in node:
            return node['recipe_book_content@bc_brewing_common.root_panel']
        for v in node.values():
            r = find_content(v)
            if r:
                return r
    elif isinstance(node, list):
        for v in node:
            r = find_content(v)
            if r:
                return r
    return None


if __name__ == '__main__':
    main()
