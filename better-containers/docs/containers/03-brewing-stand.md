# 03 — Brewing stand

The brewing stand is a full custom layout, with a brewing guide and recipe book. This guide covers the screen and its hook.
The potion logic is covered in three guides:

- [11 — Brewing guide overview](../11-brewing-guide-overview.md)
- [12 — Potions and factories](../12-brewing-factories-and-potions.md)
- [13 — Recipe book](../13-brewing-recipe-book.md)

## At a glance

| Field | Value |
|---|---|
| Vanilla screen | Brewing stand |
| File | `ui/brewing_stand_screen.json` (vanilla override, keep the name) |
| Hook paths | `brewing_stand_panel` (removes `root_panel`, inserts the recipe book and inventory), `brewing_panel_top_half` (adds the management row) |
| Inserted controls | `bc_brewing_recipe_book.recipe_book`, `common.root_panel` (inventory half), `bc_management_toggles.primary_management_toggles`, `bc_brewing_recipe_book.layout_toggle` |

## What the hook does

1. **Removes** the vanilla `root_panel` from `brewing_stand_panel`.
2. **Inserts** a horizontal `screen_stack_panel` before `flying_item_renderer` (a vanilla control, so the insertion point depends on it).
   The stack holds the recipe book panel on the left, and the inventory half on the right.
3. **Adds** the management row to `brewing_panel_top_half`.

The inventory half reuses a vanilla panel (`common.root_panel`) and adds the layout toggle from the recipe book.

## Dependencies

- `flying_item_renderer` and `brewing_panel_top_half` are vanilla names. If the game renames them, the hook fails.
- The pack controls in `brewing/` must exist. Run the validator after any change to them.

## Change this container

- **Change the recipe book position:** swap the two children of `screen_stack_panel`.
- **Change the brewing slots:** see [11](../11-brewing-guide-overview.md) and [12](../12-brewing-factories-and-potions.md).
- **Change the recipe book:** see [13](../13-brewing-recipe-book.md).

## Testing checklist

- [ ] The brewing stand opens with the recipe book on the left
- [ ] The layout toggle switches the recipe book's layout
- [ ] Ingredient, fuel, and potion slots accept items
- [ ] A potion brews and its name and effect text appear
- [ ] The management row appears in the top half

## Troubleshooting

- **Brewing stand is blank or misplaced:** check the `flying_item_renderer` insertion point and the names of the two hook paths.
- **Potion names are missing:** check the `%brewing.*` lang keys (see [16](../16-localization.md)).
- **Recipe book is missing:** check that `recipe_book.json` is loaded (it is listed in `_ui_defs.json`).

## Status

The brewing stand is the most custom of the containers. Its guide and recipe book are where most future work goes.
