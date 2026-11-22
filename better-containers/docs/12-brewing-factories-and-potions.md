# 12 — Potions and factories

A **factory** builds one slot for one potion or ingredient. The brewing guide has factories for every potion type,
in three forms: potion, splash potion, and lingering potion.

## Potion factories (`potion_slot.json`)

| Group | Controls | Notes |
|---|---|---|
| Result slots | `potion_factory`, `splash_potion_factory`, `lingering_potion_factory` | The potion after brewing |
| Ingredient slots | `potion_ingredient_factory`, `splash_potion_ingredient_factory`, `lingering_potion_ingredient_factory` | The ingredient that starts the brew |
| Special items | `water_bottle`, `awkward_potion`, `night_vision_potion`, `invisibility_potion`, and others | Each uses the shared container item template |

## Modifier factories (`modifier_slot.json`)

Each potion has up to four modifier factories:

- `duration_potion_factory`, `duration_splash_potion_factory`, `duration_lingering_potion_factory`
- `potency_potion_factory`, `potency_splash_potion_factory`, `potency_lingering_potion_factory`
- `duration_ingredient_*` and `potency_ingredient_*` for the ingredient version of each

They come from `bc_brewing_potion_slot` and show the potion's duration or potency level.

## Potion flags (`brewing_factories.json`)

`brewing_factories` holds the bindings that set each flag:

- `potion_bindings`, `splash_potion_bindings`, `lingering_potion_bindings`
- `duration_potion_bindings`, `potency_potion_bindings`, and their splash and lingering versions

Each binding sets a flag such as `#__is_strength_key`. `$factory_bindings_index` is used to build the names of the
potion item controls (`potion_item_<index>01` and so on).

## Item IDs

Every potion reads its item ID from the global variables, for example `$bc_brewing:potion_of_strength` (see [14](14-variables-and-item-ids.md)).

## Adding a potion, the short version

1. Add its item ID to `_global_variables.json` as `$bc_brewing:potion_of_<name>`.
2. Add its lang keys to every file in `texts/` (see [16](16-localization.md)).
3. Add its flag to `text_keys` in `brewing_common.json` and to a binding in `brewing_factories.json`.
4. Add its result factory in `potion_slot.json`, and its duration and potency factories in `modifier_slot.json`.
5. Add its entry to the recipe grid. See [18 — How to add a potion](18-how-to-add-a-potion.md) for the full steps.
