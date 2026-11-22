# 16 — Localization

## The language files

`texts/` has 28 locale files, named by locale (`en_US.lang`, `de_DE.lang`, `zh_CN.lang`, and so on).
`en_US.lang` is the reference. It has 108 keys, and every other language has exactly the same keys.

Each line is `key=value`. Lines that start with `#` are comments.

```
brewing.potion.damageBoost=Potion of Strength
brewing.effect.whenDrank=When Applied:
```

## How keys are used

The UI JSON refers to a key with a `%` prefix, for example `"%brewing.potion.nightVision"`. The game replaces it with the
translated text. A value can combine several keys and `§` color codes, as the brewing potions do (see [12](12-brewing-factories-and-potions.md)).

Key prefixes follow the feature:

| Prefix | Used for |
|---|---|
| `brewing.potion.*`, `brewing.splash.*`, `brewing.linger.*` | Potion names |
| `brewing.effect.*` | Effect names and descriptions |
| `brewing.ingredient.*` | Ingredient names |
| `brewing.attribute.*` | Attribute names |

## What the validator checks

- Every language file has exactly the keys in `en_US.lang`.
- No key appears twice in one file.
- Every `%key` used in the UI JSON exists in `en_US.lang`.

## Adding a language

1. Copy `texts/en_US.lang` to the new locale name (for example `texts/pt_PT.lang`).
2. Translate each value. **Keep every key name exactly as it is.**
3. Keep `§` codes and `%` placeholders in the same order.
4. Run `python3 tools/validate_pack.py pack`. It must report 0 errors.

## Changing an existing string

1. Edit the value in `texts/en_US.lang`.
2. Edit the same key in every other language, or leave the old text until someone translates it.
3. Validate, then check the text in game. Long strings can overflow their panel.
