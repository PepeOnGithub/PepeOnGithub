# 06 — Toggles, item data and shared building blocks

These files in `pack/ui/pepe/core/` are used by more than one screen. Change them with care:
a change here affects chests, the smithing table, and the brewing guide.

## `_global.json` (namespace `_global`)

Shared controls for search fields, redstone content, and the toggle/radio/button mappings.

| Control | Role |
|---|---|
| `redstone_content` | Layout for redstone-related screen content |
| `input_panel_overlay`, `input_panel_with_index`, `text_edit_control` | Input panel and text field used by search boxes |
| `mappings` | Shared mapping that `button`, `input_panel_overlay`, and `button_visuals` inherit from |
| `button`, `button_visuals` | Standard button with its visual states |
| `toggle`, `radio` | Toggle and radio-group controls. The radio uses `$radio_toggle_group` |
| `toggle_texture_template` | Texture settings for toggles |

Variables: `$toggle_group_default_selected`, `$toggle_group_forced_index`, `$toggle_default_state`,
`$toggle_is_hover`, `$icon_color`, `$icon_path`, `$consume_event`, `$button_output_action`.

## `item_data.json` (namespace `item_data`)

Four **move buttons** per item, each one doing a different action:

| Button | Output action |
|---|---|
| `move_one` | move one item |
| `move_two` | move two items |
| `move_all` | move the whole stack |
| `drop_one` / `drop_all` | drop one / the whole stack |

`item_movement_factory` builds a 100%×100% panel with five input areas. Each area uses
`input_area_template` and sets `$movement_action_control`. The area is visible only when its
toggle state matches (`#toggle_state` → `#visible`).

`$hover_control` selects the hover highlight. The default is `common.highlight_slot_panel`.

## `toggle_manager.json` (namespace `toggle_manager`)

The management toggles at the top of a container: reset, move, drop, and the status label.

| Control | Role |
|---|---|
| `primary_management_toggles` | Main toggle row. Hooked into the anvil, beacon, smithing, and chest screens |
| `right_row_toggles` | Right-hand toggles, used by chests |
| `button_holder_template` | Template for one button (reset, move, drop) |

Variables set the look: `$button_default_texture`, `$button_hover_texture`, `$button_pressed_texture`,
`$icon_texture_*`, `$row_icon_*`, `$status_label_*`, `$toggle_label_*`, `$management_toggle_size`.

Shared textures live in `textures/ui/pepe/buttons/` and `textures/ui/pepe/smithing/` (see 09).

## `uic.json` (namespace `uic`)

Navigation tabs and scroll areas. Variables: `$navigation_tabs`, `$scroll_content`,
`$tab_text_panel`. Left tabs inherit from `common_tabs.tab_left`.

## Adding a new button to a shared row

1. Copy one `*_toggles` entry in `toggle_manager.json` and rename it.
2. Set its `$button_output_action` (in `_global.json` style) to the vanilla container action.
3. Add its texture if it needs a new one (see 09).
4. Insert it into the row with `insert_back` on the parent `controls` array.
5. Run the validator, then test on a chest and on a smithing table.
