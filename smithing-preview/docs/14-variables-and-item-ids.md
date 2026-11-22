# 14 — Variables and item IDs

`ui/_global_variables.json` holds the values many screens share: item IDs, and the brewing item names. Keeping them in one file means
you change an item in one place, not in every screen.

## Groups

| Group | Examples | Used by |
|---|---|---|
| Tab icons | `$armor_items_tab_item_id`, `$smithing_template_tab_item_id`, `$mineral_items_tab_item_id` | Tab icons on the smithing table |
| Armor pieces | `$leather_helmet_item_id` … `$netherite_boots_item_id` | Armor slots and the armor preview |
| Trims | `$sentry_trim_item_id` … `$bolt_trim_item_id` | Trim items on the smithing table |
| Materials | `$diamond_item_id`, `$emerald_item_id`, `$netherite_ingot_item_id` | Material items |
| Brewing items | `$sp_brewing:potion`, `$sp_brewing:splash_potion`, `$sp_brewing:nether_wart` | Brewing guide and the compat bridge |
| Potions | `$sp_brewing:potion_of_strength`, `$sp_brewing:potion_of_swiftness`, … | Recipe book and the potion slots |

The file holds 103 variables. Run the validator if you want to confirm the file parses.

## Naming

- Item IDs: `$<item>_item_id`, for example `$diamond_item_id`.
- Brewing items: `$sp_brewing:<name>`. The colon is part of the name. Keep it exactly.
- Armor, trim, and material IDs keep the vanilla item name in them, so you can find them with search.

## Adding an item

1. Find the item's numeric ID for your target Minecraft version.
2. Add `"$<name>_item_id": <number>` to `_global_variables.json`.
3. Use `$<name>_item_id` in the control that shows it.
4. Validate and test in game. The validator checks the JSON, not whether the number is the right item.

## Numbers used by more than one name

Some numbers are used by two names. That's allowed when a tab and an item share an ID, but check them in game:

| Number | Names |
|---|---|
| 347 | `$armor_items_tab_item_id`, `$iron_chestplate_item_id` |
| 351 | `$armor_preview_button_item_id`, `$diamond_chestplate_item_id` |
| 534 | `$mineral_items_tab_item_id`, `$nether_quartz_item_id` |
| 696 | `$smithing_template_tab_item_id`, `$netherite_upgrade_item_id` |

If the wrong item appears, check these first.

## Where the IDs come from

The IDs in this file were carried over from the original upload and were not verified against game data. The validator can't check them.
If an item looks wrong in game, look up its ID for the version you are targeting.
