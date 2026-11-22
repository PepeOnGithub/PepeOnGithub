# 10 — Shared controls

These files define controls used by more than one screen. Change them carefully: an edit here affects the smithing table,
the chests, and the brewing guide.

## `shared/shared_controls.json` (`sp_shared`)

Buttons, toggles, radio groups, and input panels.

| Control | Role |
|---|---|
| `mappings` | Shared base that `button`, `input_panel_overlay`, and `button_visuals` inherit from |
| `button`, `button_visuals` | Standard button and its visual states |
| `toggle`, `radio` | Toggle and radio group (`radio` builds on `toggle` and uses `$radio_toggle_group`) |
| `toggle_texture_template` | Texture set for toggles |
| `input_panel_overlay`, `input_panel_with_index`, `text_edit_control` | Search and text inputs |
| `redstone_content` | Layout for redstone-related screen content |

## `shared/item_movement.json` (`sp_item_movement`)

Move and drop buttons for each item.

| Control | Action |
|---|---|
| `move_one` | Move one item |
| `move_two` | Move two items |
| `move_all` | Move the whole stack |
| `drop_one`, `drop_all` | Drop one, or the whole stack |

`item_movement_factory` builds five areas, one per action, each using `input_area_template`. An area is visible
only when its toggle is on (`#toggle_state` → `#visible`). `$hover_control` picks the hover highlight.

## `shared/management_toggles.json` (`sp_management_toggles`)

The management row at the top of a container: reset, move, drop, and a status label.

| Control | Role |
|---|---|
| `primary_management_toggles` | Main row. Hooked into the anvil, beacon, smithing table, and chest screens |
| `right_row_toggles` | Right-hand toggles, used by chests |
| `button_holder_template` | One management button |

Look and size come from variables: `$button_*_texture`, `$icon_texture_*`, `$row_icon_*`, `$status_label_*`, `$toggle_label_*`, `$management_toggle_size`.
Textures for this row are under `textures/smithing_preview/buttons/`, `icons/`, and `backgrounds/` (see [15](15-textures-and-fonts.md)).

## `shared/navigation.json` (`sp_navigation`)

Title bar, tabs, and scroll areas.

| Control | Role |
|---|---|
| `title_bar` | Title bar with an icon and text |
| `title_label` | Title text |
| `navigation_tabs` | Tab list |
| `tab_left_button` | Tab in a left-hand list (inherits `common_tabs.tab_left`) |
| `tab_icon_frame` | Frame around a tab icon |
| `tab_toggle_light` | Light toggle used as a tab |
| `tab_toolbar` | Toolbar behind the tab buttons |
| `scroll_content` | Scrollable content |
| `tabbed_text_screen` | Screen with a title and tabbed text |
| `inventory_icon_image`, `recipe_book_icon_image` | Icons (vanilla textures) |

## Adding a new shared button

1. Copy `button_holder_template` (management) or `toggle` (shared) as an instance with `@`, not by copying its body.
2. Set its output action, for example `$button_output_action` on a `button`.
3. Add its texture under `textures/smithing_preview/buttons/` if it needs one.
4. Insert it into a row with `insert_back` on the parent `controls` array.
5. Validate, then test on a chest and on the smithing table.
