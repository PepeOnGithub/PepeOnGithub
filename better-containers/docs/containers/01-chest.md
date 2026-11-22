# 01 — Chest (single and double)

Chests are the most used containers in the pack. A single chest has 27 slots (three rows), and a double chest has 54 (six rows).
The pack builds both from the same parts, so one fix applies to both.

## At a glance

| Field | Value |
|---|---|
| Vanilla screens | Small chest, large (double) chest |
| File | `ui/chest_screen.json` (vanilla override, keep the name) |
| Hook paths | `small_chest_panel/root_panel/chest_panel`, `large_chest_panel/root_panel/chest_panel` |
| Operation | `insert_front` into `controls` |
| Inserted controls | `bc_chest_single.container_elements` (small), `bc_chest_double.container_elements` (large) |
| Pack files | `ui/better_containers/containers/chest_single.json`, `chest_double.json` |

`chest_screen.json` has `/* */` comments. They're valid Bedrock and are kept on purpose. See [Comments](#comments-in-chest_screenjson).

## What the pack adds

- **Overlay rows** for move one, move two, move all, drop one, and drop all. They sit over each slot row and respond to clicks.
- **Highlight and pressed states** for each row and for the hotbar.
- **A search field**: the chest variables (`$search_field_*`) suggest one. Confirm in game whether it shows.

## Layouts

| Control | Rows | What it covers |
|---|---|---|
| `9x1_overlays` | 1 | One slot row |
| `9x3_overlays` | 3 | Three slot rows |
| `9x6_overlays` | 6 | Six slot rows (double chest) |
| `hotbar_*_overlay` | 1 | The hotbar row |

`chest_double` reuses `chest_single`'s `container_elements` and adds `9x6_overlays`. A double chest is a single chest with more rows.

## Variables

| Variable | Purpose |
|---|---|
| `$item_collection_name` | Collection the slots bind to: `container_items`, `inventory_items`, or `hotbar_items` |
| `$collection_index` | Index within that collection |
| `$row_index_offset` | Offset of the row's first slot |
| `$inventory_overlay_offset`, `$hotbar_overlay_offset`, `$container_overlay_offset` | Where each grid sits |
| `$*_slot_highlight_control`, `$*_slot_pressed_control` | Controls for hover and pressed states |
| `$output_action` | The action a click sends |

## Change this container

- **Change one row's look:** edit its `row_*_overlay` template in `chest_single.json`. The double chest picks up the change.
- **Change the double chest only:** edit `chest_double.json`. Its rows come from `chest_single`, so change that file only for shared parts.
- **Remove the overlays from one chest size:** delete its `modifications` entry from `chest_screen.json`.

## Testing checklist

- [ ] A single chest opens, and its three rows show overlays
- [ ] A double chest opens, and its six rows show overlays
- [ ] Move one, move two, move all, drop one, and drop all each work on a stack
- [ ] The hotbar row responds to clicks
- [ ] Shift-click still moves items between the chest and the inventory

## Troubleshooting

- **A chest looks blank or stacked:** check both hook paths. A vanilla update that renames `root_panel` or `chest_panel` breaks them.
- **Only one size works:** the other hook path is probably wrong. Check the path for that size.
- **Overlays are misaligned:** check the `*_overlay_offset` variables for that size.

## Comments in `chest_screen.json`

The file keeps its `/* */` comment at the top. The formatter would remove it, so the file is kept as written.

## Status

The chest uses the overlay design above, and nothing else. Future work: a per-chest layout (for example, a different hotbar style) would be a new template in `containers/` (see [21](../21-known-issues-and-roadmap.md)).
