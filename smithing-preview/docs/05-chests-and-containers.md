# 05 — Chests and containers

## Files

| File | Role |
|---|---|
| `ui/chest_screen.json` | Vanilla override. Inserts the chest content into `small_chest_panel` and `large_chest_panel` |
| `ui/pepe/chests/single_chest_content.json` | `single_chest_content` — 1-row, 3-row, and hotbar layouts |
| `ui/pepe/chests/double_chest_content.json` | `double_chest_content` — 6-row layout, built on the single chest |
| `ui/anvil_screen.json`, `ui/beacon_screen.json` | Vanilla overrides that add the shared toggle manager to their inventory panel |
| `ui/cartography_screen.json`, `ui/enchanting_screen.json`, `ui/grindstone_screen.json`, `ui/loom_screen.json`, `ui/furnace_screen.json`, `ui/horse_screen.json`, `ui/inventory_screen.json`, `ui/trade_2_screen.json`, `ui/redstone_screen.json` | Vanilla overrides in the pack. Their content was not changed in this rework, so review them individually |

## Chest content

`single_chest_content` defines these overlay layouts, one per slot grid:

- `9x1_overlays` — one row
- `9x3_overlays` — three rows
- `hotbar_*` — the hotbar row, with its own move and drop overlays

Each row has overlays for **move one**, **move two**, **move all**, **drop one**, and **drop all**.
They're built from `row_move_*_overlay` / `row_drop_*_overlay` templates.

`double_chest_content` reuses the single chest's `container_elements` and adds `9x6_overlays`.
A double chest is therefore a single chest with more rows, not a separate design.

## Variables that control a chest

| Variable | Used for |
|---|---|
| `$item_collection_name` | Which collection the slots bind to (`container_items`, `inventory_items`, `hotbar_items`) |
| `$collection_index` | Index inside that collection |
| `$row_index_offset` | Offset for the row's first slot |
| `$inventory_overlay_offset`, `$hotbar_overlay_offset`, `$container_overlay_offset` | Where each grid sits |
| `$*_slot_highlight_control`, `$*_slot_pressed_control` | Which control renders hover and pressed states |
| `$output_action` | The button action sent on click (for example a container auto-place) |

## Vanilla hooks

Both chest files hook into `chest_panel`, so the overlays are added inside each vanilla chest:

- `small_chest_panel/root_panel/chest_panel` → `single_chest_content.container_elements`
- `large_chest_panel/root_panel/chest_panel` → `double_chest_content.container_elements`

If a chest looks blank or stacked, check these two paths first. A vanilla update that renames
`root_panel` or `chest_panel` would break them.

## Comments in `chest_screen.json`

`ui/chest_screen.json` contains `/* */` comments. Bedrock accepts them. The file is kept
byte-for-byte as uploaded, because the formatter would have removed the comments.
