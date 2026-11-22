# 04 — Smithing screen

## Files

| File | Namespace | Role |
|---|---|---|
| `ui/smithing_table_2_screen.json` | (vanilla override) | Hooks the pack into the vanilla smithing table panel |
| `ui/pepe/smithing/smithing.json` | `smithing` | Smithing table panels: item-id pickers and tab layouts |
| `ui/pepe/smithing/smithing_arc.json` | `smithing_arc` | The armor-slot arc with rotation and slider states |
| `ui/pepe/core/toggle_manager.json` | `toggle_manager` | Shared management toggles (also used by chests) |
| `ui/pepe/core/item_data.json` | `item_data` | Move / drop buttons (also used by chests) |

## How the vanilla screen is hooked

`smithing_table_2_screen.json` does two things:

1. Removes the vanilla `root_panel` from `smithing_table_panel`.
2. Adds a custom control (`smithing.r_fi52`) in its place, and inserts the
   `toggle_manager.primary_management_toggles` into the screen inventory.

If the smithing table looks wrong after a vanilla update, check these two modifications first.

## Smithing panels (`smithing.json`)

The file builds an item-id picker. Each picker is an item renderer with two variables, which
are set per item:

- `$item_id` — the numeric ID of the item, multiplied by 65536 into `#item_id`.
- `$item_id_aux` — the aux/data value, combined with `#item_id` into the full ID.

The item IDs come from `ui/_global_variables.json` (see 08).

Control names here are machine-generated IDs (for example `l_0oe`, `gho_66`, `dl_s72`). They are
kept as-is because they are referenced in many places. The table below lists the ones
that have a clear role:

| Control | Role |
|---|---|
| `smithing.l_0oe` | Item renderer wrapper (16×16, centred). Used as button content |
| `smithing.gho_66` | Light-content toggle built from `common_toggles` |
| `smithing.lg_1e` | Horizontal stack panel (100%c × 22) for toggle rows |
| `smithing.dl_s72` | Panel that holds the toggle stacks |
| `uic.lg_0t` | Left tab, inherited from `common_tabs.tab_left` (defined in `core/uic.json`) |

## Armor arc (`smithing_arc.json`)

Each armor slot uses one `p_9a6u` template with two inputs:

- `$rotation_x` — tilt of the arc item (for example `-60`, `-30`, `0`, `30`, `60`).
- `$slider_value_y` — index (0–4) matching the slider state.

`$rotation_y` and `$slider_value` (set to `-180` and `0`) control the arc's overall orientation.
The `e3_d7x` panel holds all five positions. `j2-wh` is the outer container (60×42, offset `0, -10`).

## Editing tips

- To change an item shown on the smithing table, edit the ID in `_global_variables.json`,
  not in `smithing.json`.
- To change the arc's positions, change `$rotation_x` and `$slider_value_y` together.
  If you add a position, you also need a new slider step (`#slider_steps`).
