# 11 — Brewing guide overview

The brewing guide replaces the brewing stand's inventory with a potion-aware layout and adds a recipe book that
shows which ingredients make which potion. It's the largest part of the pack.

## Map of the folder

```
ui/better_containers/brewing/
├── brewing_common.json       bc_brewing_common      shared controls, text keys, blank building blocks
├── brewing_factories.json    bc_brewing_factories   maps potion keys to their flags
├── brewing_toggles.json      bc_brewing_toggles     tab and layout toggles
├── slots/
│   ├── potion_slot.json      bc_brewing_potion_slot       ingredient, result, and fuel slots + potion factories
│   └── modifier_slot.json    bc_brewing_modifier_slot     duration and potency variants
└── recipe_book/
    ├── recipe_book.json      bc_brewing_recipe_book      recipe book panel and tabs
    └── recipe_grid.json      bc_brewing_recipe_grid      recipe grid
```

Also in `compat/`: `container_item_bridge.json` connects the brewing slots to the container item template (see [13](13-brewing-recipe-book.md)).

Read the guides in this order: **11 (this one)**, then [12 — Potions and factories](12-brewing-factories-and-potions.md),
then [13 — Recipe book](13-brewing-recipe-book.md).

## How a potion appears

1. **Key.** Each potion has a flag, for example `#__is_night_vision_key`. `brewing_factories` sets it.
2. **Text.** `brewing_common.text_keys` maps each flag to a lang string. Each value uses `%brewing.*` keys from `texts/`,
   for example `%brewing.potion.nightVision` plus the effect duration line. `§` codes add color.
3. **Slot.** `potion_slot` picks the right factory from the flag. Duration and potency variants come from `modifier_slot`.
4. **Recipe book.** `recipe_grid` lays out the recipes, using the grid variables and the toggle indexes.

Flags come in two families:

- `#__is_<name>_key`: is this item the potion or ingredient `<name>`?
- `#__potency_is_<name>_key`: the potency-variant flag for the same potion.

## Slots and the `variables` selector

`potion_slot` uses a `variables` array. Each entry checks the item collection and picks a control:

| Collection | Slot |
|---|---|
| `brewing_input_item` | `brewing_ingredient_item_slot` |
| `brewing_result_items` | `brewing_result_item_slot` |
| `brewing_fuel_item` | `fuel_input_slot` |

## Where things are defined

| Thing | Defined in | Namespace |
|---|---|---|
| Potion text keys | `brewing_common.json` (`text_keys`) | `bc_brewing_common` |
| Potion flags | `brewing_factories.json` | `bc_brewing_factories` |
| Result, ingredient, and fuel slots | `potion_slot.json` | `bc_brewing_potion_slot` |
| Duration and potency | `modifier_slot.json` | `bc_brewing_modifier_slot` |
| Recipe book and grid | `recipe_book/` | `bc_brewing_recipe_book`, `bc_brewing_recipe_grid` |

## Vanilla-facing names

The brewing guide refers to a few vanilla controls that the pack doesn't define, for example `brewing_guide_toggle` and
`flying_item_renderer`. They're listed as unresolved by the validator (see [17](17-validation-and-building.md)). They work
because the game provides them. If a vanilla update renames them, the guide breaks, so check these first.
