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
                      'nether_gold_ore', 'quartz_ore', 'redstone_ore', 'ancient_debris', 'raw_copper', 'raw_gold', 'raw_iron',
                      'deepslate_coal_ore', 'deepslate_copper_ore', 'deepslate_diamond_ore', 'deepslate_emerald_ore',
                      'deepslate_gold_ore', 'deepslate_iron_ore', 'deepslate_lapis_ore', 'deepslate_redstone_ore'], '$is_smoker'),
    ('blocks', 'Blocks', ['cobblestone', 'sand', 'clay', 'netherrack', 'basalt', 'cobbled_deepslate',
                          'stone_bricks', 'deepslate_bricks', 'deepslate_tiles', 'stone', 'sandstone', 'red_sandstone',
                          'nether_brick', 'polished_blackstone_bricks', 'quartz_block', 'wet_sponge'], None),
    ('nature', 'Nature', ['cactus', 'chorus_fruit', 'sea_pickle', 'clay_ball', 'resin_clump', 'oak_log', 'spruce_log', 'birch_log',
                         'jungle_log', 'acacia_log', 'dark_oak_log', 'mangrove_log', 'cherry_log', 'pale_oak_log'], None),
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
    'spears': 'Spears of every tier, using the same material as that tier',
    'copper_gear': 'Copper helmet, chestplate, leggings, boots, sword, pickaxe, axe, shovel, hoe (copper ingot)',
    'iron_armors': 'Iron and chainmail helmet, chestplate, leggings, boots (iron ingot)',
    'golden_armors': 'Golden helmet, chestplate, leggings, boots (gold ingot)',
    'diamond_armors': 'Diamond helmet, chestplate, leggings, boots (diamond)',
    'netherite_armors': 'Netherite helmet, chestplate, leggings, boots (netherite ingot)',
    'repair_materials': 'Planks fix wood and shields. Cobblestone, cobbled deepslate or blackstone fix stone. Leather, ingots and diamonds fix the rest',
    'repair_amount': 'Each material restores 25 percent durability. Two damaged items of one kind can also be combined',
}
FORMAT_CODES = [('k', 'Obfuscated'), ('l', 'Bold'), ('m', 'Strikethrough'), ('n', 'Underline'), ('o', 'Italic'), ('r', 'Reset')]
COLOR_CODES = [('0', 'Black'), ('1', 'Dark Blue'), ('2', 'Dark Green'), ('3', 'Dark Aqua'), ('4', 'Dark Red'),
               ('5', 'Dark Purple'), ('6', 'Gold'), ('7', 'Gray'), ('8', 'Dark Gray'), ('9', 'Blue'), ('a', 'Green'),
               ('b', 'Aqua'), ('c', 'Red'), ('d', 'Light Purple'), ('e', 'Yellow'), ('f', 'White')]
# Vanilla-named override files. "screen" is the variable block set on the screen root (Glacier does the same
# for blast furnace and smoker); each placement is (path inside the screen, guide root name, guide namespace).
FURNACE_PLACEMENT = ('right_panel/furnace_screen_inventory', 'furnace_guide', 'bc_furnace_guide')
INFO_PLACEMENTS = {
    'beacon': ('beacon_screen.json', 'beacon_panel/root_panel/beacon_inventory'),
    'cartography': ('cartography_screen.json', 'cartography_panel/root_panel/cartography_screen_inventory'),
    'grindstone': ('grindstone_screen.json', 'grindstone_panel/root_panel/grindstone_screen_inventory'),
    'horse': ('horse_screen.json', 'horse_panel/root_panel'),
    'inventory': ('inventory_screen.json', 'player_inventory'),
    'loom': ('loom_screen.json', 'right_panel/loom_screen_inventory'),
    'trade': ('trade_2_screen.json', 'right_panel/trade_screen_inventory'),
    'stonecutter': ('stonecutter_screen.json', 'right_panel/stonecutter_screen_inventory'),
}
HOOK_SPECS = [
    {'file': 'furnace_screen.json', 'screen': None, 'placements': [FURNACE_PLACEMENT]},
    {'file': 'blast_furnace_screen.json', 'screen': {'blast_furnace_screen': {'$is_blast_furnace': True}},
     'placements': []},
    {'file': 'smoker_screen.json', 'screen': {'smoker_screen': {'$is_smoker': True}},
     'placements': []},
    {'file': 'enchanting_screen.json', 'screen': None, 'placements': [
        ('enchanting_panel/root_panel/enchanting_screen_inventory', 'enchanting_guide', 'bc_enchanting_guide')]},
    {'file': 'anvil_screen.json', 'screen': None, 'placements': [
        ('anvil_panel/root_panel/anvil_screen_inventory', 'anvil_guide', 'bc_anvil_guide')]},
    # smithing: the guide and management toggles live inside smithing/smithing_table.json (the vanilla
    # root_panel is removed, so a path below it would never apply)
    {'file': 'smithing_table_2_screen.json', 'screen': None, 'placements': []},
    *[{'file': f, 'screen': None, 'placements': [(path, f'{n}_info', f'bc_{n}_info')]}
      for n, (f, path) in INFO_PLACEMENTS.items()],
    {'file': 'chest_screen.json', 'screen': None, 'placements': [
        ('small_chest_panel/root_panel/chest_panel', 'chest_guide', 'bc_chest_guide'),
        ('large_chest_panel/root_panel/chest_panel', 'chest_guide', 'bc_chest_guide')]},
]


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
    root_panel = {'type': 'stack_panel', 'orientation': 'vertical', 'size': [width, '100%c'], 'layer': 2, 'anchor_from': 'top_left', 'anchor_to': 'top_right', 'offset': [4, 0],
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
    burn = read_json(os.path.join(ROOT, 'data', 'container_info.json'))['fuel_burn']
    for key, title, items, hidden in FURNACE_TABS:
        controls = grid([(i, i) for i in items])
        if key == 'fuel':
            controls += text_panel_controls('bc_furnace_guide', [f'bc_furnace_guide.burn.{i}' for i in burn])
        tabs.append((key, f'bc_furnace_guide.tab.{key}', controls, hidden))
    body = tabbed('bc_furnace_guide', 'furnace_guide', 'bc_furnace_guide.title', CELL * COLUMNS, tabs,
                  defaults={'$is_blast_furnace|default': False, '$is_smoker|default': False})
    smelt = read_json(os.path.join(ROOT, 'data', 'container_info.json'))['smelt_time']
    root_controls = body['furnace_guide']['controls']
    smelt_rows = [{f'smelt_{k}@bc_furnace_guide.text_row': {'$line_text': f'%bc_furnace_guide.smelt.{k}'}}
                  for k in smelt]
    root_controls[1:1] = smelt_rows
    body['progress_bar'] = {
        'type': 'panel', 'size': ['100%', 6], 'controls': [
            {'track': {'type': 'panel', 'size': ['100%', 4], 'controls': [
                {'fill': {'type': 'image', 'texture': 'textures/ui/White', 'color': '$bar_color',
                          'size': ['100%', '100%'], 'clip_direction': '$bar_clip',
                          'bindings': [{'binding_name': '$bar_binding', 'binding_name_override': '#clip_ratio',
                                        'binding_condition': 'always'}]}}]}}]}
    # progress bars sit above the tab bar, in the root panel
    root = body['furnace_guide']
    root['controls'].insert(1, {'flame_bar@bc_furnace_guide.progress_bar': {
        '$bar_binding': '#furnace_flame_ratio', '$bar_clip': 'left', '$bar_color': [1.0, 0.55, 0.0]}})
    root['controls'].insert(2, {'arrow_bar@bc_furnace_guide.progress_bar': {
        '$bar_binding': '#furnace_arrow_ratio', '$bar_clip': 'left', '$bar_color': [0.47, 0.78, 0.47]}})
    return body


def enchanting(enchants):
    """enchants: list of (lang key, roman max level). Each row: icon, name, description, max level."""
    rows = []
    for i, (key, level) in enumerate(enchants):
        rows.append({f'row_{i}@bc_enchanting_guide.enchant_row': {
            '$name_text': f'%{key}', '$desc_text': f'%bc_enchanting_guide.desc.{key}', '$level_text': level}})
    top = {'namespace': 'bc_enchanting_guide',
           'enchant_row': {'type': 'panel', 'size': ['100%', 26], 'controls': [
               {'book_icon@bc_item_cell.item_cell': {'$item_id': '$enchanted_book_item_id', 'size': [14, 14],
                                                     'offset': [0, 2]}},
               {'name_label': {'type': 'label', 'text': '$name_text', 'size': ['100%-70px', 10],
                               'offset': [18, 0], 'font_size': 'small'}},
               {'desc_label': {'type': 'label', 'text': '$desc_text', 'size': ['100%-18px', 10],
                               'offset': [18, 11], 'font_size': 'small'}},
               {'level_label': {'type': 'label', 'text': '$level_text', 'size': [40, 10],
                                'anchor_from': 'top_right', 'anchor_to': 'top_right', 'font_size': 'small'}}]}}
    top['enchanting_guide'] = {'type': 'stack_panel', 'orientation': 'vertical', 'size': [CELL * COLUMNS, '100%c'], 'layer': 2, 'anchor_from': 'top_left', 'anchor_to': 'top_right', 'offset': [4, 0], 'controls': [
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
    entries = read_json(os.path.join(ROOT, 'data', 'nametag_entries.json'))
    keys = [f'bc_anvil_guide.nametag.{i}' for i in range(len(entries))] or ['bc_anvil_guide.nametag.empty']
    tabs.append(('nametag', 'bc_anvil_guide.tab.nametag', text_panel_controls('bc_anvil_guide', keys), None))
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
    top['chest_guide'] = {'type': 'stack_panel', 'orientation': 'vertical', 'size': [60, '100%c'], 'layer': 2, 'anchor_from': 'top_left', 'anchor_to': 'top_right', 'offset': [4, 0], 'controls': [
        {'title_label': {'type': 'label', 'text': '%bc_chest_guide.title', 'size': ['100%', 12]}},
        {'search_box@bc_shared.text_edit_control': {}},
        {'auto_place_all_label@bc_chest_guide.action_label': {'$action_text': '%bc_chest_guide.auto_place_all'}},
        {'auto_place_all_button@bc_shared.button': {'$button_output_action': 'button.container_auto_place',
                                                    'size': [56, 14]}},
        {'auto_place_one_label@bc_chest_guide.action_label': {'$action_text': '%bc_chest_guide.auto_place_one'}},
        {'auto_place_one_button@bc_shared.button': {'$button_output_action': 'button.container_auto_place_one',
                                                    'size': [56, 14]}}]}
    return top


def info_guide(name, spec):
    """A plain information panel for a container: title and one wrapped text line per entry."""
    ns = f'bc_{name}_info'
    rows = [{f'line_{i}@{ns}.info_row': {'$line_text': f'%{ns}.line.{i}'}} for i in range(len(spec['lines']))]
    return {
        'namespace': ns,
        'info_row': {'type': 'label', 'text': '$line_text', 'size': ['100%', 'default'], 'font_size': 'small'},
        f'{name}_info': {'type': 'stack_panel', 'orientation': 'vertical', 'size': [CELL * COLUMNS, '100%c'], 'layer': 2, 'anchor_from': 'top_left', 'anchor_to': 'top_right', 'offset': [4, 0], 'controls': [
            {'title_label': {'type': 'label', 'text': f'%{ns}.title', 'size': ['100%', 12]}},
            {'info_lines': {'type': 'stack_panel', 'orientation': 'vertical', 'size': ['100%', 'default'],
                            'controls': rows}}]},
    }


# ---------------------------------------------------------------- lang text
def strings():
    descriptions = read_json(os.path.join(ROOT, 'data', 'enchantment_descriptions.json'))
    nametags = read_json(os.path.join(ROOT, 'data', 'nametag_entries.json'))
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
    info = read_json(os.path.join(ROOT, 'data', 'container_info.json'))
    for name, spec in info['containers'].items():
        s[f'bc_{name}_info.title'] = spec['title']
        for i, line in enumerate(spec['lines']):
            s[f'bc_{name}_info.line.{i}'] = line
    for k, text in info['smelt_time'].items():
        s[f'bc_furnace_guide.smelt.{k}'] = f'Smelt time, {k.replace("_", " ")}: {text}'
    for k, text in info['fuel_burn'].items():
        s[f'bc_furnace_guide.burn.{k}'] = f'{k.replace("_", " ").title()}: {text}'
    for key, text in descriptions.items():
        s[f'bc_enchanting_guide.desc.{key}'] = text
    for i, entry in enumerate(nametags):
        s[f'bc_anvil_guide.nametag.{i}'] = entry
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
    info = read_json(os.path.join(ROOT, 'data', 'container_info.json'))['containers']
    for name, spec in info.items():
        write_json(os.path.join(PACK, 'ui', 'better_containers', 'containers', f'{name}_info.json'),
                   info_guide(name, spec))

    write_json(os.path.join(PACK, 'ui', 'better_containers', 'shared', 'item_cell.json'), {
        'namespace': 'bc_item_cell',
        'item_cell': {'type': 'panel', 'size': [CELL, CELL], '$item_id|default': 0, '$item_id_aux|default': 0,
                      'controls': [{'icon@common.item_renderer': {
                          'size': [CELL - 2, CELL - 2], 'anchor_from': 'center', 'anchor_to': 'center',
                          'property_bag': {'#item_id': '($item_id * 65536)', '#full_item_id': '$item_id_aux'},
                          'bindings': [{'binding_type': 'view', 'source_property_name': '(#full_item_id + #item_id)',
                                        'target_property_name': '#item_id_aux'}]}}]}})

    # 4. hooks into the vanilla screens (append, never duplicate). Files that do not exist yet are created.
    for spec in HOOK_SPECS:
        path = os.path.join(PACK, 'ui', spec['file'])
        raw = open(path, encoding='utf-8').read() if os.path.exists(path) else '{}'
        comment = None
        m = re.search(r'/\*.*?\*/', raw, flags=re.S)
        if m:
            comment = m.group(0)
            raw = raw.replace(comment, '', 1)
        hook = json.loads(re.sub(r'//[^\n]*', '', raw))
        if spec['screen']:
            hook.update(spec['screen'])
        for path_key, guide, ns in spec['placements']:
            entry = hook.setdefault(path_key, {'modifications': []})
            mods = entry['modifications']
            ref = f'{guide}@{ns}.{guide}'
            if not any(ref in json.dumps(mod) for mod in mods):
                mods.append({'array_name': 'controls', 'operation': 'insert_back', 'value': {ref: {}}})
        write_json(path, hook, leading_comment=comment)

    # 5. register the new UI files
    dpath = os.path.join(PACK, 'ui', '_ui_defs.json')
    defs = read_json(dpath)['ui_defs']
    info_names = list(read_json(os.path.join(ROOT, 'data', 'container_info.json'))['containers'])
    wanted = ['ui/better_containers/shared/item_cell.json'] + [
        f'ui/better_containers/containers/{n}_guide.json' for n in guides] + [
        f'ui/better_containers/containers/{n}_info.json' for n in info_names]
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
    import translate_ui_labels  # re-apply translated short labels over the English placeholders
    translate_ui_labels.main()
    import apply_translations  # re-apply stored long-text translations
    apply_translations.main()


if __name__ == '__main__':
    main()
