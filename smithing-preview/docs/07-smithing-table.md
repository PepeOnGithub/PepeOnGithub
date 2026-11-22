# 07 — Smithing table

## Files

| File | Namespace | Role |
|---|---|---|
| `ui/smithing_table_2_screen.json` | vanilla override | Hooks the pack into the vanilla smithing table |
| `ui/smithing_preview/smithing/smithing_table.json` | `sp_smithing_table` | Panels, item pickers, and the tab bar |
| `ui/smithing_preview/smithing/armor_arc.json` | `sp_armor_arc` | The armor arc (see [08](08-armor-arc.md)) |
| `ui/smithing_preview/shared/management_toggles.json` | `sp_management_toggles` | Reset / move / drop toggles, also used on other screens |
| `ui/smithing_preview/shared/item_movement.json` | `sp_item_movement` | Move and drop buttons, also used on chests |

## How the vanilla screen is hooked

`smithing_table_2_screen.json` does two things:

1. Removes the vanilla `root_panel` from `smithing_table_panel`.
2. Inserts `sp_smithing_table.smithing_table_screen` in its place, and adds
   `sp_management_toggles.primary_management_toggles` to the screen inventory.

If the smithing table looks wrong after a game update, check these two modifications first.

## Controls

| Control | Role |
|---|---|
| `smithing_table_screen` | Root control for the whole pack-owned smithing layout |
| `item_picker_panel` | Holds the item pickers (one per selectable item) |
| `item_picker_toggle` | Toggle that shows one item as its content |
| `item_picker_icon` | 16×16 item renderer. Takes `$item_id` and `$item_id_aux` |
| `toggle_row` | Horizontal row for toggles |
| `smithing_tabs` | The tab bar. Built from `sp_navigation.navigation_tabs` |
| `armor_tab_icon`, `template_tab_icon`, `mineral_tab_icon` | Tab icons, each with a fixed item ID for its tab |
| `armor_preview_button` | Armor preview button, shown with its own hover and pressed textures |
| `tab_text_stack` | Stack holding the tab text |
| `armor_arc_group` | Groups the armor arc's three parts (primary, secondary, and slider) |

## Item IDs

Every item shown here reads its numeric ID from `ui/_global_variables.json` (for example `$armor_items_tab_item_id`).
The smithing table never hard-codes an ID. See [14 — Variables and item IDs](14-variables-and-item-ids.md).

## Editing checklist

1. Change item IDs in `_global_variables.json`, not in `smithing_table.json`.
2. To add a picker, copy `item_picker_toggle` with `@`, set its `$button_content` to `sp_smithing_table.item_picker_icon`, and add it to `item_picker_panel`.
3. To change a tab, edit its icon control and its `$tab_view_binding_name`. Keep the tab order in `smithing_tabs`.
4. Validate, then test every tab in game.
