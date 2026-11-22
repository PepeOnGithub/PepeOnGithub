# 13 — Recipe book

The recipe book shows which ingredients make which potion. It has tabs for each potion type, a grid of recipes,
and layout toggles.

## Files

| File | Namespace | Role |
|---|---|---|
| `recipe_book/recipe_book.json` | `sp_brewing_recipe_book` | Panel, tabs, layout toggles, and the book's background |
| `recipe_book/recipe_grid.json` | `sp_brewing_recipe_grid` | The grid of recipes |
| `compat/container_item_bridge.json` | none (not in `_ui_defs`) | Adds the brewing mapping to the vanilla container item |

## Controls

| Control | Role |
|---|---|
| `recipe_book` | The recipe book panel |
| `recipe_grid` | The grid of recipes |
| `grid_filler_panel` | Fills empty grid cells |
| `highlight_slot_panel` | Highlight when a slot is hovered |
| `center_item_icon` | Item icon in the middle of a slot |
| `tab_template` | One tab in the recipe book |
| `potion_tab_toggle`, `splash_potion_tab_toggle`, `lingering_potion_tab_toggle` | Tabs per potion type. (The recipe book also refers to `potion_tab`, which is not defined in the pack; see [21](21-known-issues-and-roadmap.md).) |
| `layout_toggle`, `recolourful_layout_toggle` | Switch between the two recipe book layouts |
| `recolourful_recipe_book` | Alternative look for the recipe book |

## Grid variables

| Variable | Purpose |
|---|---|
| `$brewing_grid_size`, `$brewing_grid_dimensions` | Size of the grid |
| `$brewing_grid_position_0` … `$brewing_grid_position_19` | 20 named positions, one per grid slot |
| `$grid_item_size`, `$grid_item_renderer_offset`, `$grid_item_renderer_anchor_point` | Item size and placement |
| `$has_duration`, `$has_potency` | Whether a recipe shows the duration or potency variant |
| `$duration_toggle_index`, `$potency_toggle_index` | Which toggle a recipe uses |

## Textures

Recipe book textures are under `textures/smithing_preview/brewing/recipe_book/`:

- `background.png` — the book background
- `sprites/` — tab, button, filter, slot, and text-field sprites
- `sprites/bedrock/` — Bedrock-style button sprites

Vanilla textures used by the book (for example `textures/ui/recipe_book_icon`) come from the game.

## Changing the layout

1. Move a recipe by changing its `$brewing_grid_position_*` value, not its control.
2. Change the grid size in `$brewing_grid_size` and `$brewing_grid_dimensions` together.
3. Test both layouts (`layout_toggle` and `recolourful_layout_toggle`).
