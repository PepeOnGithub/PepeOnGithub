# 08 — Armor arc

The armor arc is the curved row of armor slots shown on the smithing table. It lives in `ui/smithing_preview/smithing/armor_arc.json`
(namespace `sp_armor_arc`).

## Structure

There are two arcs. Each one has the same parts:

| Part | Primary | Secondary | Role |
|---|---|---|---|
| Arc | `arc_primary` | `arc_secondary` | Outer container (60×42, offset up by 10) |
| Positions | `arc_primary_positions` | `arc_secondary_positions` | The five slot positions |
| Slot | `arc_primary_slot` | `arc_secondary_slot` | One position, with its rotation and slider value |
| Slot base | `arc_primary_slot_base` | `arc_secondary_slot_base` | Base control with the screen's entrance and exit animations |

`arc_slider` is a shared slider (`common.slider`). `armor_arc_group` on the smithing table holds both arcs and the slider.

## Variables

| Variable | Meaning |
|---|---|
| `$rotation_x` | Tilt of a slot, for example `-60`, `-30`, `0`, `30`, `60` |
| `$rotation_y` | Turn of the arc. The primary arc starts at `30`, the secondary at `-30` |
| `$slider_value` | Slider position that selects this slot |
| `$slider_value_y` | Index of the slot within its arc (0–4) |
| `$slider_name` | Name of the slider this arc follows |

## Why the two arcs are separate

The primary arc reads its item data from the `smithing_table_result_items` collection. The secondary arc reads a view
property instead, and the two arcs have different defaults. Because the bindings aren't identical, they can't be merged into one
template without changing behavior.
They're kept as two parallel sets. A future version can merge them into one parameterized template, once you have tested the change in game (see [21](21-known-issues-and-roadmap.md)).

## Changing the arc

1. To change a slot's tilt, edit `$rotation_x` on its `arc_*_slot` instance.
2. To add a position, add one `arc_*_slot` with its own `$slider_value_y`. Also add the matching step to the slider.
3. To change the arc's overall angle, change `$rotation_y` on the `arc_*_slot` template.
4. Validate, then test with the slider at every position.
