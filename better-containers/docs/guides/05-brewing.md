# 05 — Brewing guide

The brewing guide is the most complete guide in this pack, and the reference for the others. It's documented in three parts:

- [11 — Brewing guide overview](../11-brewing-guide-overview.md): how the guide is put together
- [12 — Potions and factories](../12-brewing-factories-and-potions.md): the potion factories and flags
- [13 — Recipe book](../13-brewing-recipe-book.md): the recipe book, grid, and tabs

## Filter

The reference brewing stand adds a filter dropdown with four choices. The pack's recipe book has tabs for each potion
type instead of a dropdown. The four filter choices are:

| Choice | Shows |
|---|---|
| All Potions | Every potion |
| Mixed Potions | Potions that mix two effects |
| Positive Potions | Potions with beneficial effects |
| Negative Potions | Potions with harmful effects |

If you add the dropdown, use these four choices, and show each as a `%lang` key (see [16](../16-localization.md)).

## Ingredients

Each ingredient has a hover text in the reference guide. The pack shows ingredient names through the `%brewing.ingredient.*` keys,
so a hover text is a `text_keys` entry with the same key (see [12](../12-brewing-factories-and-potions.md)).

## Status

Done: tabs, recipe grid, potion text, and the brewing slots. Not built: the filter dropdown.

## Checklist

- [ ] Each potion tab shows its recipes
- [ ] The filter (once built) shows only the matching potions
- [ ] Ingredient hover text shows each ingredient's name
