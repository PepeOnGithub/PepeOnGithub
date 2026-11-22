# 07 — Brewing guide

The brewing guide is the largest part of the pack. It replaces the brewing stand's inventory with
a potion-aware layout and adds a recipe book that shows what each potion needs.

## Files (in load order as `_ui_defs.json` lists them)

| File | Namespace | Role |
|---|---|---|
| `brewing_guide/brewing_global.json` | `brewing_global` | Shared controls: text keys, empty panels, custom renderer, root panel |
| `brewing_guide/factory_bindings.json` | `factory_bindings` | Bindings that map potion keys to potion properties |
| `brewing_guide/brewing_toggle.json` | `brewing_toggle` | Toggle templates: tabs, layout toggles, secondary toggles |
| `brewing_guide/inventory_area/brewing_potion_slot.json` | `brewing_potion_slot` | Ingredient, result, and fuel slots, plus potion factories |
| `brewing_guide/inventory_area/modifier_brewing_potion_slot.json` | `modifier_brewing_potion_slot` | Duration and potency variants of each potion |
| `brewing_guide/recipe_book_area/brewing_recipe_book.json` | `brewing_recipe_book` | Recipe book panel, tabs, layout toggles |
| `brewing_guide/recipe_book_area/brewing_recipe_book_grid.json` | `brewing_recipe_book_grid` | Recipe grid: one slot per recipe |

Also: `compat/compatibility_container_item.json` (not in `_ui_defs`, see 13) bridges the brewing
slots to the container item template.

## How a potion is shown

1. **Key.** Each potion has a key such as `#__is_night_vision_key`. The factory bindings set it.
2. **Text.** `brewing_global.text_keys` maps that key to a lang string. Each value is a `%brewing.*`
   key from `texts/`, for example `%brewing.potion.nightVision` plus a line for the effect
   duration (`%brewing.effect.nightVision (3:00)`). Colors use `§` codes.
3. **Slot.** `brewing_potion_slot` picks the right potion factory from the key.
   Duration and potency variants come from `modifier_brewing_potion_slot`.
4. **Recipe book.** `brewing_recipe_book_grid` lays out the recipe, using `$grid_item`,
   `$has_duration`, `$has_potency`, and the toggle indexes.

Potion-specific flags follow two patterns:
- `#__is_<name>_key` — is this item the potion or ingredient `<name>`?
- `#__potency_is_<name>_key` — the potency-variant flag for the same potion.

## Slots and the `variables` selector

`brewing_potion_slot` uses a `variables` array whose entries check `$item_collection`:

| Collection | Slot |
|---|---|
| `brewing_input_item` | `brewing_ingredient_item_slot` |
| `brewing_result_items` | `brewing_result_item_slot` |
| `brewing_fuel_item` | `fuel_input_slot` |

The compat bridge (`compatibility_container_item.json`) adds the same mapping to the vanilla
container item, using `$base_id` (default `$brewing_guide:potion`) and `$potion_prefix`.

## Recipe book options

- `$brewing_grid_size`, `$brewing_grid_dimensions`, `$brewing_grid_position_0`…`_19` — grid
  layout. There are 20 named grid positions.
- `$brewing_*_texture` and `$*_image` — textures for the tabs, slots, filter, and text field.
  Several point to `assets/brewing_guide/...` (see 09).
- `$tab_toggle_type`, `$visible_condition`, `$slot_hover_controller`.

## Changing a potion

1. Find its item ID in `ui/_global_variables.json` (`$brewing_guide:potion_of_<name>`), see 08.
2. Add or edit its text in `texts/en_US.lang` (`brewing.potion.<name>`), then in every other lang (10).
3. Check its key in `brewing_global.json` `text_keys` and `factory_bindings.json`.
4. Check its slot in `brewing_potion_slot.json` and its duration/potency variants in `modifier_brewing_potion_slot.json`.
5. Validate, then test the potion on a brewing stand and in the recipe book.
