# 02 — Smithing table

The smithing table has the largest custom layout in the pack. Its full design is in two guides:

- [07 — Smithing table](../07-smithing-table.md): panels, item pickers, and the tab bar
- [08 — Armor arc](../08-armor-arc.md): the arc, its slots, and the slider

## At a glance

| Field | Value |
|---|---|
| Vanilla screen | Smithing table |
| File | `ui/smithing_table_2_screen.json` (vanilla override, keep the name) |
| Hook paths | `smithing_table_panel` (removes `root_panel`), `smithing_table_panel/root_panel/smithing_table_screen_inventory` |
| Operations | `remove` the vanilla `root_panel`, `insert_back` the pack screen, `insert_front` the management row |
| Inserted controls | `bc_smithing_table.smithing_table_screen`, `bc_management_toggles.primary_management_toggles` |

## What changes

The pack swaps the vanilla root panel for its own `smithing_table_screen`. That screen holds the item pickers, the tab bar
(`smithing_tabs`), and the armor arc group. The management row is added on top of the inventory.

## Why this hook is different

Most containers only get an extra row. The smithing table removes the vanilla root panel, so **the vanilla layout is
replaced**. If a vanilla update changes the smithing table, this is where the layout will break first.

## Change this container

- **Change the layout:** edit `ui/better_containers/smithing/smithing_table.json`.
- **Change the arc:** edit `ui/better_containers/smithing/armor_arc.json` (see [08](../08-armor-arc.md)).
- **Restore the vanilla root:** remove the `remove` modification from `smithing_table_2_screen.json`. The pack layout then sits on top of the vanilla one, so check it looks right before you ship.

## Testing checklist

- [ ] The screen opens without a missing-control error
- [ ] Each tab in `smithing_tabs` selects the matching item set
- [ ] The armor arc responds to the slider at all five positions
- [ ] Items can be placed in and removed from the input slots
- [ ] The management row appears on the right

## Troubleshooting

- **Blank smithing table:** the `remove` of `root_panel` ran, but `smithing_table_screen` is missing. Check the name in `insert_back`.
- **Tabs show no icon:** the item ID in `_global_variables.json` is wrong, or the tab icon control has the wrong name. See [14](../14-variables-and-item-ids.md).
- **Arc is in the wrong place:** check `arc_*_positions` and the `$rotation_*` values.

## Status

The smithing table is fully custom. It's the best place to test a new layout approach before using it on other containers.
