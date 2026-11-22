# 03 — Naming conventions

Consistent names make the pack easier to read, search, and validate. These rules apply to every new name.

## Namespaces

- Every pack namespace starts with `sp_` (short for Smithing Preview). That keeps it separate from vanilla names,
  which the game also loads.
- After the prefix, use the feature name in snake_case: `sp_smithing_table`, `sp_brewing_recipe_book`.
- The namespace matches the file name without the prefix, so `containers/chest_single.json` → `sp_chest_single`.

| File | Namespace |
|---|---|
| `shared/shared_controls.json` | `sp_shared` |
| `shared/item_movement.json` | `sp_item_movement` |
| `shared/navigation.json` | `sp_navigation` |
| `shared/management_toggles.json` | `sp_management_toggles` |
| `containers/chest_single.json` | `sp_chest_single` |
| `containers/chest_double.json` | `sp_chest_double` |
| `smithing/smithing_table.json` | `sp_smithing_table` |
| `smithing/armor_arc.json` | `sp_armor_arc` |
| `brewing/brewing_common.json` | `sp_brewing_common` |
| `brewing/brewing_factories.json` | `sp_brewing_factories` |
| `brewing/brewing_toggles.json` | `sp_brewing_toggles` |
| `brewing/slots/potion_slot.json` | `sp_brewing_potion_slot` |
| `brewing/slots/modifier_slot.json` | `sp_brewing_modifier_slot` |
| `brewing/recipe_book/recipe_book.json` | `sp_brewing_recipe_book` |
| `brewing/recipe_book/recipe_grid.json` | `sp_brewing_recipe_grid` |

## Controls

- Use **snake_case** and describe the **role**, not the appearance: `item_picker_icon`, `arc_primary_slot`.
- Start with the feature when it helps search: `arc_`, `tab_`, `chest_`, `brewing_`.
- Use a suffix for the kind of thing it is:

| Suffix | Meaning | Example |
|---|---|---|
| `_template` | Reusable control, intended for `@` inheritance | `button_holder_template` |
| `_factory` | Creates one item or potion slot from variables | `potion_factory` |
| `_bindings` | A list of bindings only | `potion_bindings` |
| `_overlays` | A group of highlight or move overlays | `9x3_overlays` |
| `_panel` | A plain panel container | `tab_text_panel` |
| `_toggle` / `_toggles` | A toggle, or a row of toggles | `tab_toggle_light`, `primary_management_toggles` |
| `_icon` / `_image` | An image or item icon | `armor_tab_icon`, `inventory_icon_image` |
| `_screen` | The root of a whole screen | `smithing_table_screen` |

- Do not use generated IDs (`l_0oe`, `gho_66`). Those were removed in this version. Never add a new one.
- Do not reuse a vanilla control name for a pack control. Pick a name the vanilla UI doesn't have.

## Variables

- Use `$` plus snake_case: `$item_id`, `$rotation_x`, `$tab_icon`.
- Put a default on any variable that a template can be used without: `"$item_id|default": 0`.
- Keep global item IDs in `ui/_global_variables.json` and name them `$<item>_item_id`.
- Brewing items use `$sp_brewing:<name>`, for example `$sp_brewing:potion`.

## Files

- snake_case, lowercase, no spaces, no version numbers (`chest_single.json`, not `chest_single_v2.json`).
- Name a file after the one thing it defines.
- Vanilla override files keep the vanilla name (`anvil_screen.json`). Do not rename them.

## Textures

- Paths are lowercase, with folders for the type: `textures/smithing_preview/icons/copper.png`.
- Name a texture after what it shows. Use the folder for its type, not a suffix.
- Don't use spaces or capitals in new names. Vanilla textures are the only exception, and they stay as the game names them.

## Quick checklist for a new name

1. Does the namespace start with `sp_`?
2. Is the control named after its role, in snake_case, with a suffix that matches its kind?
3. Is the variable `$snake_case` and does it have a default if needed?
4. Is the file in the right feature folder and named after its namespace?
5. Does the texture sit in `textures/smithing_preview/<type>/`?
