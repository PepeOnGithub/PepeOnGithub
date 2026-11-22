# 18 — How to add a potion

This is a step-by-step guide. Do the steps in order, and validate after each group.

## Before you start

- Know the potion's item ID for your Minecraft version, and its name in English.
- Choose a short name. This guide uses `example` as the placeholder; replace it everywhere.

## 1. Item ID

In `ui/_global_variables.json`, add:

```json
"$sp_brewing:potion_of_example": 123
```

Use the real ID. The validator doesn't check it.

## 2. Language

In `texts/en_US.lang`, add the three lines the potion needs:

```
brewing.potion.example=Potion of Example
brewing.splash.example=Splash Potion of Example
brewing.linger.example=Lingering Potion of Example
```

Add the same keys to every other file in `texts/`. Translate them, or copy the English value until someone translates it.
Run the validator to confirm the keys match.

## 3. Text and flag

In `ui/smithing_preview/brewing/brewing_common.json`, add the flag's text to `text_keys`, following the pattern of an existing potion
(for example `#__is_strength_key`). Use `%brewing.potion.example` and, if the effect has a duration, `%brewing.effect.example`.

## 4. Binding

In `ui/smithing_preview/brewing/brewing_factories.json`, add a binding for the new flag, copying an existing one and changing its names.

## 5. Slots

- In `ui/smithing_preview/brewing/slots/potion_slot.json`, add the result and ingredient factories for the potion, copying an existing potion.
- In `ui/smithing_preview/brewing/slots/modifier_slot.json`, add its duration and potency factories.

Use `@` to instantiate existing templates. Don't copy a template's body.

## 6. Recipe grid

In `ui/smithing_preview/brewing/recipe_book/recipe_grid.json`, add a recipe in an unused `$brewing_grid_position_*`. Check `recipe_book.json`
for the matching tab.

## 7. Validate and test

```bash
python3 tools/validate_pack.py pack
python3 tools/build_mcpack.py
```

Then test in game: brew the potion, check its name and effect text, and find it in the recipe book.

## Checklist

- [ ] Item ID added to `_global_variables.json`
- [ ] Lang keys added to every file in `texts/`
- [ ] Text key and flag added to `brewing_common.json`
- [ ] Binding added to `brewing_factories.json`
- [ ] Result, ingredient, duration, and potency factories added
- [ ] Recipe grid position added
- [ ] Validator reports 0 errors
- [ ] Tested in game
