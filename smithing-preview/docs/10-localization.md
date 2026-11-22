# 10 — Localization

## Files

`texts/` has 28 language files, named by locale (`en_US.lang`, `de_DE.lang`, `zh_CN.lang`, …).
`en_US.lang` is the reference: it has **108 keys**, and every other language has the same keys.

Format: one `key=value` per line. Lines starting with `#` are comments.

```
brewing.potion.damageBoost=Potion of Strength
brewing.effect.whenDrank=When Applied:
```

## How keys are used

UI JSON refers to a key with a `%` prefix, for example `"%brewing.potion.nightVision"`.
The game replaces it with the translated text. A value can combine several keys and `§` color
codes, as the brewing potions do (see 07).

## Rules the validator enforces

- Every language file has exactly the keys in `en_US.lang` (no missing, no extra keys).
- No key is duplicated within a file.
- Every `%key` used in the UI JSON exists in `en_US.lang`.

## Adding a language

1. Copy `texts/en_US.lang` to the new locale name (for example `texts/pt_PT.lang`).
2. Translate each value, but **keep the key names exactly as they are**.
3. Keep `§` codes and `%` placeholders in the same order.
4. Run `python3 tools/validate_pack.py pack`. It must report 0 errors.

## Changing an existing string

1. Edit the value in `texts/en_US.lang`.
2. Edit the same key in every other language file, or leave the old text in place until someone translates it.
3. Validate and check the text in game, including long strings, since they can overflow their panel.
