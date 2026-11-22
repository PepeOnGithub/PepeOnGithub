# 07 — Container anatomy

Every container guide uses the same shared parts. The reference pack defines them once in a base file, and each
container uses them. This pack follows the same idea: shared controls live in `ui/better_containers/shared/`.

## Shared parts

| Part | What it does | Used by |
|---|---|---|
| Tab bar with tab icons | One toggle per category | Furnace, smithing, anvil |
| Item cell | Item renderer inside a toggle | Every item grid |
| Tab text label | A label that shows when its tab is open | Every tab |
| Hover text | Shows an item's name on hover | Every item grid |
| Highlight | Outlines a slot on hover or press | Chest, every grid |
| Close and autoplace | Closes the screen and moves items to their place | Every container |
| Trash and destroy | Destroys the item in a slot, or in the trash slot | Every container |
| Layout toggle | Opens or closes the guide panel | Brewing, smithing, enchanting |
| Recipe book panel | The guide panel itself | Brewing, furnace, smithing, enchanting |

## Where the pack has these today

| Part | Pack control |
|---|---|
| Tab bar | `bc_navigation.navigation_tabs`, `bc_navigation.tab_left_button` |
| Item cell | `bc_brewing_recipe_book.recipe_grid` cells, `bc_smithing_table` item pickers |
| Management row | `bc_management_toggles.primary_management_toggles` (reset, move, drop) |
| Layout toggle | `bc_brewing_recipe_book.layout_toggle` |
| Highlight | `bc_chest_single` highlight controls |

The trash and destroy part and the close-and-autoplace part are not in this pack yet. Build them once in `shared/`, and each container will use them.

## Rules for shared parts

1. A shared part lives in `shared/`, and every container instantiates it with `@`.
2. A container sets only the variables it needs.
3. A change to a shared part is a change for every container. Test each container after you change one.
