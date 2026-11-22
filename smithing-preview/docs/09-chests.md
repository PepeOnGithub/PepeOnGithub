# 09 — Chests

## Files

| File | Namespace | Role |
|---|---|---|
| `ui/chest_screen.json` | vanilla override | Inserts the chest content into the small and large chest panels |
| `ui/smithing_preview/containers/chest_single.json` | `sp_chest_single` | 1-row, 3-row, and hotbar layouts |
| `ui/smithing_preview/containers/chest_double.json` | `sp_chest_double` | 6-row layout, built on `chest_single` |
| `ui/anvil_screen.json`, `ui/beacon_screen.json` | vanilla overrides | Add the shared management toggles to the screen |
| `ui/cartography_screen.json`, `ui/enchanting_screen.json`, `ui/grindstone_screen.json`, `ui/loom_screen.json`, `ui/furnace_screen.json`, `ui/horse_screen.json`, `ui/inventory_screen.json`, `ui/trade_2_screen.json`, `ui/redstone_screen.json` | vanilla overrides | Other vanilla screens in the pack. Review them individually before changing them |

## Layout

`chest_single` defines the overlay groups:

- `9x1_overlays`: one row
- `9x3_overlays`: three rows
- `hotbar_*`: the hotbar row, with its own move and drop overlays

Each row has overlays for move one, move two, move all, drop one, and drop all. Each is built from a
`row_*_overlay` template, so one fix applies to every row.

`chest_double` uses `chest_single`'s `container_elements` and adds `9x6_overlays`. A double chest is a single chest with more rows.

## Variables

| Variable | Used for |
|---|---|
| `$item_collection_name` | Which collection the slots bind to (`container_items`, `inventory_items`, `hotbar_items`) |
| `$collection_index` | Index within that collection |
| `$row_index_offset` | Offset of a row's first slot |
| `$inventory_overlay_offset`, `$hotbar_overlay_offset`, `$container_overlay_offset` | Position of each grid |
| `$*_slot_highlight_control`, `$*_slot_pressed_control` | Controls for the hover and pressed states |
| `$output_action` | The button action sent on click |

## Vanilla hooks

- `small_chest_panel/root_panel/chest_panel` gets `sp_chest_single.container_elements`.
- `large_chest_panel/root_panel/chest_panel` gets `sp_chest_double.container_elements`.

If a chest looks blank or stacked after a game update, check these two paths first.

## Comments in `chest_screen.json`

`ui/chest_screen.json` has `/* */` comments, which Bedrock accepts. The file is kept as uploaded so the comments are not lost.
