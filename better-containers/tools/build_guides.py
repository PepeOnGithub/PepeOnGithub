#!/usr/bin/env python3
"""Generate every in-game container guide panel.

Guides: furnace (furnace, blast furnace, smoker), enchanting, anvil, smithing table, chest.

Writes into pack/:
  ui/better_containers/shared/item_cell.json               shared item cell template
  ui/better_containers/containers/*_guide.json            one file per guide
  ui/<vanilla>_screen.json                                hooks that place each guide
  ui/_global_variables.json                               $<item>_item_id values (added, never overwritten)
  ui/_ui_defs.json                                        registers the new files
  texts/*.lang                                            guide strings (English copied to every locale)

Item IDs come from data/item_ids/stable-1.26.60.json (Minecraft Item ID Viewer list).
Re-run after changing a guide here. Every step is idempotent.
"""
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACK = os.path.join(ROOT, 'pack')
LIST = os.path.join(ROOT, 'data', 'item_ids', 'stable-1.26.60.json')
CELL = 18
COLUMNS = 8                      # item cells per row: 8 x 18px = 144px
TAB_W = 28

# ---------------------------------------------------------------- item lists
# (variable name without $, item label key is not needed: the cell shows the real item)
FURNACE_TABS = [
    ('foods', 'Foods', ['beef', 'porkchop', 'chicken', 'mutton', 'rabbit', 'cod', 'salmon', 'potato', 'kelp'], '$is_blast_furnace'),
    ('ores', 'Ores', ['coal_ore', 'copper_ore', 'diamond_ore', 'emerald_ore', 'gold_ore', 'iron_ore', 'lapis_ore',
                      'nether_gold_ore', 'quartz_ore', 'redstone_ore', 'ancient_debris', 'raw_copper', 'raw_gold', 'raw_iron'], '$is_smoker'),
    ('blocks', 'Blocks', ['cobblestone', 'sand', 'clay', 'netherrack', 'basalt', 'cobbled_deepslate',
                          'stone_bricks', 'deepslate_bricks', 'deepslate_tiles'], None),
    ('nature', 'Nature', ['cactus', 'chorus_fruit', 'sea_pickle', 'clay_ball', 'oak_log'], None),
    ('fuel', 'Fuel', ['coal', 'charcoal', 'coal_block', 'blaze_rod', 'lava_bucket', 'dried_kelp_block', 'bamboo',
                      'bamboo_block', 'stick'], None),
]
ARMOR = [f'{m}_{p}' for m in ['leather', 'chainmail', 'iron', 'golden', 'diamond', 'netherite']
         for p in ['helmet', 'chestplate', 'leggings', 'boots']] + ['turtle_shell']
TRIMS = ['netherite_upgrade', 'sentry', 'vex', 'wild', 'coast', 'dune', 'wayfinder', 'shaper', 'raiser', 'host',
         'ward', 'silence', 'tide', 'snout', 'rib', 'eye', 'spire', 'flow', 'bolt']
RESOURCES = ['amethyst_shard', 'copper_ingot', 'diamond', 'emerald', 'gold_ingot', 'iron_ingot', 'lapis_lazuli',
             'nether_quartz', 'netherite_ingot', 'redstone_dust', 'resin_brick']
SMITHING_TABS = [
    ('armors', 'Armors', ARMOR, None),
    ('templates', 'Smithing Templates', ['netherite_upgrade'] + TRIMS[1:], None),
    ('resources', 'Resources', RESOURCES, None),
]
# Variable base name -> viewer item name, where they differ. Trims are <name>_trim_item_id in _global_variables.
ITEM_ALIAS = {
    'turtle_shell': 'turtle_helmet', 'nether_quartz': 'quartz', 'redstone_dust': 'redstone',
    'netherite_upgrade': 'netherite_upgrade_smithing_template',
}


def var_base(name):
    """Variable base for a cell: trims are stored as <name>_trim."""
    return f'{name}_trim' if name in TRIMS[1:] else name


def viewer_name(base):
    if base.endswith('_trim'):
        return base[:-5] + '_armor_trim_smithing_template'
    return ITEM_ALIAS.get(base, base)
REPAIR_GROUPS = {
    'wooden_tools': 'Wooden pickaxe, axe, shovel, hoe, sword',
    'stone_tools': 'Stone pickaxe, axe, shovel, hoe, sword',
    'iron_tools': 'Iron pickaxe, axe, shovel, hoe, sword',
    'golden_tools': 'Golden pickaxe, axe, shovel, hoe, sword',
    'diamond_tools': 'Diamond pickaxe, axe, shovel, hoe, sword',
    'netherite_tools': 'Netherite pickaxe, axe, shovel, hoe, sword',
    'leather_armors': 'Leather helmet, chestplate, leggings, boots',
    'elytra': 'Elytra',
    'shields': 'Shield',
    'mace': 'Mace',
    'turtle_shell': 'Turtle helmet',
    'wolf_armor': 'Wolf armor',
}
FORMAT_CODES = [('k', 'Obfuscated'), ('l', 'Bold'), ('m', 'Strikethrough'), ('n', 'Underline'), ('o', 'Italic'), ('r', 'Reset')]
COLOR_CODES = [('0', 'Black'), ('1', 'Dark Blue'), ('2', 'Dark Green'), ('3', 'Dark Aqua'), ('4', 'Dark Red'),
               ('5', 'Dark Purple'), ('6', 'Gold'), ('7', 'Gray'), ('8', 'Dark Gray'), ('9', 'Blue'), ('a', 'Green'),
               ('b', 'Aqua'), ('c', 'Red'), ('d', 'Light Purple'), ('e', 'Yellow'), ('f', 'White')]
SCREEN_HOOKS = {
    'furnace': ('furnace_screen.json', [('right_panel/furnace_screen_inventory', 'furnace_guide')]),
    'enchanting': ('enchanting_screen.json', [('enchanting_panel/root_panel/enchanting_screen_inventory', 'enchanting_guide')]),
    'anvil': ('anvil_screen.json', [('anvil_panel/root_panel/anvil_screen_inventory', 'anvil_guide')]),
    'smithing': ('smithing_table_2_screen.json', [('smithing_table_panel/root_panel/smithing_table_screen_inventory', 'smithing_guide')]),
    'chest': ('chest_screen.json', [('small_chest_panel/root_panel/chest_panel', 'chest_guide'),
                                    ('large_chest_panel/root_panel/chest_panel', 'chest_guide')]),
}


# ---------------------------------------------------------------- helpers
def load_items():
    data = json.load(open(LIST, encoding='utf-8'))
    return {i['name'].split(':', 1)[1]: i['id'] for i in data['items']}


def read_json(path):
    return json.load(open(path, encoding='utf-8'))


def write_json(path, data, leading_comment=None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = json.dumps(data, indent=2, ensure_ascii=False) + '\n'
    if leading_comment:
        text = text.replace('{\n', '{\n' + leading_comment + '\n', 1)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def panel_visible(source):
    return [{'binding_type': 'view', 'source_control_name': source,
             'source_property_name': '#toggle_state', 'target_property_name': '#visible'}]


def cell(name, base):
    """One item cell. base is the variable base; the cell reads $<base>_item_id."""
    return {f'{name}_cell@bc_item_cell.item_cell': {'$item_id': f'${base}_item_id'}}


def grid(items):
    """items: list of (cell name, variable base). Returns stack rows of cells."""
    rows = []
    for r in range(0, len(items), COLUMNS):
        chunk = items[r:r + COLUMNS]
        rows.append({f'row_{r // COLUMNS}': {
            'type': 'stack_panel', 'orientation': 'horizontal', 'size': ['100%', CELL],
            'controls': [cell(n, v) for n, v in chunk]}})
    return rows


def tab_panel(key, controls, hidden=None):
    panel = {'type': 'stack_panel', 'orientation': 'vertical', 'size': ['100%', 'default'],
             'controls': controls, 'bindings': panel_visible(f'{key}_tab_toggle')}
    if hidden:
        panel['ignored'] = hidden
    return panel


def tabbed(ns, root, title_key, width, tabs, defaults=None):
    """Radio tab bar with one panel per tab. tabs: list of (key, label_key, panel_controls, hidden_expr)."""
    top = {'namespace': ns,
           'tab_label': {'type': 'label', 'text': '$tab_text', 'size': ['100%', 12], 'font_size': 'small'},
           'text_row': {'type': 'label', 'text': '$line_text', 'size': ['100%', 10], 'font_size': 'small'}}
    bar, contents = [], []
    for index, (key, label_key, controls, hidden) in enumerate(tabs):
        label = f'{key}_label'
        top[f'{label}@{ns}.tab_label'] = {'$tab_text': f'%{label_key}'}
        tab = {'type': 'panel', 'size': [TAB_W, 14],
               'controls': [{f'{key}_tab@bc_shared.radio': {
                   '$toggle_name': f'{root}_tabs', '$toggle_view_binding_name': f'{key}_tab_toggle',
                   '$toggle_group_forced_index': index, '$toggle_default_state': index == 0,
                   '$button_content': f'{ns}.{label}', 'size': [TAB_W, 14]}}]}
        if hidden:
            tab['ignored'] = hidden
        bar.append({f'{key}_tab_slot': tab})
        contents.append({f'{key}_panel': tab_panel(key, controls, hidden)})
    root_panel = {'type': 'panel', 'size': [width, 'default'], 'layer': 2,
                  'controls': [
                      {'title_label': {'type': 'label', 'text': f'%{title_key}', 'size': ['100%', 12]}},
                      {'tab_bar': {'type': 'stack_panel', 'orientation': 'horizontal', 'size': ['100%', 16],
                                   'controls': bar}},
                      {'tab_contents': {'type': 'panel', 'size': ['100%', 'default'],
                                        'controls': contents}}]}
    if defaults:
        root_panel.update(defaults)
    top[root] = root_panel
    return top


def text_panel_controls(ns, keys):
    return [{f'line_{i}@{ns}.text_row': {'$line_text': f'%{k}'}} for i, k in enumerate(keys)]


# ---------------------------------------------------------------- guides
def furnace():
    tabs = []
    for key, title, items, hidden in FURNACE_TABS:
        tabs.append((key, f'bc_furnace_guide.tab.{key}', grid([(i, i) for i in items]), hidden))
    return tabbed('bc_furnace_guide', 'furnace_guide', 'bc_furnace_guide.title', CELL * COLUMNS, tabs,
                  defaults={'$is_blast_furnace|default': False, '$is_smoker|default': False})


def enchanting(enchants):
    rows = []
    for i, (key, level) in enumerate(enchants):
        rows.append({f'row_{i}@bc_enchanting_guide.enchant_row': {
            '$name_text': f'%{key}', '$level_text': f'Max {level}'}})
    top = {'namespace': 'bc_enchanting_guide',
           'enchant_row': {'type': 'panel', 'size': ['100%', 16], 'controls': [
               {'book_icon@bc_item_cell.item_cell': {'$item_id': '$enchanted_book_item_id', 'size': [14, 14]}},
               {'name_label': {'type': 'label', 'text': '$name_text', 'size': ['100%-60px', 10],
                               'offset': [18, 0], 'font_size': 'small'}},
               {'level_label': {'type': 'label', 'text': '$level_text', 'size': [54, 10],
                                'anchor_from': 'right_middle', 'anchor_to': 'right_middle', 'font_size': 'small'}}]}}
    top['enchanting_guide'] = {'type': 'panel', 'size': [CELL * COLUMNS, 'default'], 'layer': 2, 'controls': [
        {'title_label': {'type': 'label', 'text': '%bc_enchanting_guide.title', 'size': ['100%', 12]}},
        {'scroll_view': {'type': 'scroll_view', 'size': ['100%', 120], 'controls': [
            {'scrolling_content': {'type': 'stack_panel', 'orientation': 'vertical', 'size': ['100%', 'default'],
                                   'controls': rows}}]}}]}
    return top


def anvil():
    tabs = []
    repair_lines = [{f'{g}_line@bc_anvil_guide.text_row': {'$line_text': f'%bc_anvil_guide.group.{g}'}}
                    for g in REPAIR_GROUPS]
    tabs.append(('repair', 'bc_anvil_guide.tab.repair', repair_lines, None))
    tabs.append(('format', 'bc_anvil_guide.tab.format',
                 text_panel_controls('bc_anvil_guide', [f'bc_anvil_guide.format.{c}' for c, _ in FORMAT_CODES]), None))
    tabs.append(('color', 'bc_anvil_guide.tab.color',
                 text_panel_controls('bc_anvil_guide', [f'bc_anvil_guide.color.{c}' for c, _ in COLOR_CODES]), None))
    tabs.append(('nametag', 'bc_anvil_guide.tab.nametag',
                 text_panel_controls('bc_anvil_guide', ['bc_anvil_guide.nametag.empty']), None))
    return tabbed('bc_anvil_guide', 'anvil_guide', 'bc_anvil_guide.title', CELL * COLUMNS, tabs)


def smithing():
    tabs = []
    for key, title, names, hidden in SMITHING_TABS:
        cells = [(n, var_base(n)) for n in names]
        tabs.append((key, f'bc_smithing_guide.tab.{key}', grid(cells), hidden))
    return tabbed('bc_smithing_guide', 'smithing_guide', 'bc_smithing_guide.title', CELL * COLUMNS, tabs)


def chest():
    top = {'namespace': 'bc_chest_guide',
           'action_label': {'type': 'label', 'text': '$action_text', 'size': ['100%', 10], 'font_size': 'small'}}
    top['chest_guide'] = {'type': 'panel', 'size': [60, 'default'], 'layer': 2, 'controls': [
        {'title_label': {'type': 'label', 'text': '%bc_chest_guide.title', 'size': ['100%', 12]}},
        {'search_box@bc_shared.text_edit_control': {}},
        {'auto_place_all_label@bc_chest_guide.action_label': {'$action_text': '%bc_chest_guide.auto_place_all'}},
        {'auto_place_all_button@bc_shared.button': {'$button_output_action': 'button.container_auto_place',
                                                    'size': [56, 14]}},
        {'auto_place_one_label@bc_chest_guide.action_label': {'$action_text': '%bc_chest_guide.auto_place_one'}},
        {'auto_place_one_button@bc_shared.button': {'$button_output_action': 'button.container_auto_place_one',
                                                    'size': [56, 14]}}]}
    return top


# ---------------------------------------------------------------- lang text
def strings():
    s = {
        'bc_furnace_guide.title': 'Furnace Guide',
        'bc_furnace_guide.tab.foods': 'Foods', 'bc_furnace_guide.tab.ores': 'Ores',
        'bc_furnace_guide.tab.blocks': 'Blocks', 'bc_furnace_guide.tab.nature': 'Nature',
        'bc_furnace_guide.tab.fuel': 'Fuel',
        'bc_enchanting_guide.title': 'Enchantments',
        'bc_anvil_guide.title': 'Anvil Guide',
        'bc_anvil_guide.tab.repair': 'Repairable', 'bc_anvil_guide.tab.format': 'Formatting',
        'bc_anvil_guide.tab.color': 'Colors', 'bc_anvil_guide.tab.nametag': 'Nametag',
        'bc_anvil_guide.nametag.empty': 'No nametag entries are defined yet.',
        'bc_smithing_guide.title': 'Smithing Guide',
        'bc_smithing_guide.tab.armors': 'Armors',
        'bc_smithing_guide.tab.templates': 'Templates',
        'bc_smithing_guide.tab.resources': 'Resources',
        'bc_chest_guide.title': 'Chest',
        'bc_chest_guide.auto_place_all': 'Auto place all',
        'bc_chest_guide.auto_place_one': 'Auto place one',
    }
    for g, desc in REPAIR_GROUPS.items():
        s[f'bc_anvil_guide.group.{g}'] = f'{g.replace("_", " ").title()}: {desc}'
    for c, name in FORMAT_CODES:
        s[f'bc_anvil_guide.format.{c}'] = f'§{c}{name}'
    for c, name in COLOR_CODES:
        s[f'bc_anvil_guide.color.{c}'] = f'§{c}{name}'
    return s


# ---------------------------------------------------------------- main
def main():
    items = load_items()

    # 1. variables: every item cell needs $<base>_item_id. Add missing ones, never change an existing value.
    vpath = os.path.join(PACK, 'ui', '_global_variables.json')
    variables = read_json(vpath)
    bases = {'enchanted_book'}
    bases |= {b for _, _, its, _ in FURNACE_TABS for b in its}
    bases |= {var_base(n) for _, _, names, _ in SMITHING_TABS for n in names}
    added = 0
    for base in sorted(bases):
        name = viewer_name(base)
        if name not in items:
            raise SystemExit(f'item {name!r} (for ${base}_item_id) is not in the item list')
        key = f'${base}_item_id'
        if key not in variables:
            variables[key] = items[name]
            added += 1
        elif variables[key] != items[name]:
            raise SystemExit(f'{key} is {variables[key]} but the item list says {items[name]}; fix by hand')
    write_json(vpath, variables)
    print('variables added:', added)

    # 2. enchanting rows from the reference list (lang key + max level, no description text)
    enchants = []
    data_path = os.path.join(ROOT, 'data', 'enchantments.json')
    if os.path.exists(data_path):
        enchants = [tuple(x) for x in read_json(data_path)]
    if not enchants:
        raise SystemExit('data/enchantments.json is missing or empty')

    # 3. the guide files
    guides = {
        'furnace': furnace(),
        'enchanting': enchanting(enchants),
        'anvil': anvil(),
        'smithing': smithing(),
        'chest': chest(),
    }
    for name, body in guides.items():
        out = os.path.join(PACK, 'ui', 'better_containers', 'containers', f'{name}_guide.json')
        write_json(out, body)

    write_json(os.path.join(PACK, 'ui', 'better_containers', 'shared', 'item_cell.json'), {
        'namespace': 'bc_item_cell',
        'item_cell': {'type': 'panel', 'size': [CELL, CELL], '$item_id|default': 0, '$item_id_aux|default': 0,
                      'controls': [{'icon@common.item_renderer': {
                          'size': [CELL - 2, CELL - 2], 'anchor_from': 'center', 'anchor_to': 'center',
                          'property_bag': {'#item_id': '($item_id * 65536)', '#full_item_id': '$item_id_aux'},
                          'bindings': [{'binding_type': 'view', 'source_property_name': '(#full_item_id + #item_id)',
                                        'target_property_name': '#item_id_aux'}]}}]}})

    # 4. hooks into the vanilla screens (append, never duplicate)
    for name, (file, placements) in SCREEN_HOOKS.items():
        path = os.path.join(PACK, 'ui', file)
        raw = open(path, encoding='utf-8').read()
        comment = None
        m = re.search(r'/\*.*?\*/', raw, flags=re.S)
        if m:
            comment = m.group(0)
            raw = raw.replace(comment, '', 1)
        hook = json.loads(re.sub(r'//[^\n]*', '', raw))
        for path_key, guide in placements:
            entry = hook.setdefault(path_key, {'modifications': []})
            mods = entry['modifications']
            ref = f'{guide}@bc_{name}_guide.{guide}'
            if not any(ref in json.dumps(mod) for mod in mods):
                mods.append({'array_name': 'controls', 'operation': 'insert_back',
                             'value': {f'{guide}@bc_{name}_guide.{guide}': {}}})
        write_json(path, hook, leading_comment=comment)

    # 5. register the new UI files
    dpath = os.path.join(PACK, 'ui', '_ui_defs.json')
    defs = read_json(dpath)['ui_defs']
    wanted = ['ui/better_containers/shared/item_cell.json'] + [
        f'ui/better_containers/containers/{n}_guide.json' for n in guides]
    for entry in wanted:
        if entry not in defs:
            defs.append(entry)
    write_json(dpath, {'ui_defs': defs})

    # 6. strings in every language file
    s = strings()
    for path in sorted(glob.glob(os.path.join(PACK, 'texts', '*.lang'))):
        lines = open(path, encoding='utf-8').read().split('\n')
        existing = {l.split('=', 1)[0] for l in lines if '=' in l and not l.lstrip().startswith('#')}
        new = [f'{k}={v}' for k, v in s.items() if k not in existing]
        if new:
            open(path, 'w', encoding='utf-8', newline='\n').write(
                '\n'.join(lines).rstrip('\n') + '\n' + '\n'.join(new) + '\n')
    print('guides written:', ', '.join(guides))


if __name__ == '__main__':
    main()
