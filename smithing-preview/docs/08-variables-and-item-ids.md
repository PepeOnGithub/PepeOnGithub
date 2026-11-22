# 08 — Variables and item IDs

`ui/_global_variables.json` holds 103 global values. Other UI files read them as `$name`.
Keep all numeric IDs here, so changes don't require editing screen code.

## Sections

| Group | Examples | Used by |
|---|---|---|
| Tab icons | `$armor_items_tab_item_id` (347), `$smithing_template_tab_item_id` (696), `$mineral_items_tab_item_id` (534) | Tab buttons on the smithing table |
| Armor pieces | `$leather_helmet_item_id` (338) … `$netherite_boots_item_id` (628) | Armor slots and the armor preview |
| Trims | `$sentry_trim_item_id` (697) … `$flow_trim_item_id` (713), `$bolt_trim_item_id` (714) | Trim items on the smithing table |
| Materials | `$diamond_item_id` (306), `$emerald_item_id` (523), `$netherite_ingot_item_id` (624) | Material items |
| Brewing items | `$brewing_guide:potion` (430), `$brewing_guide:splash_potion` (571), `$brewing_guide:lingering_potion` (572), `$brewing_guide:nether_wart` (294), … | Brewing guide and the compat bridge |
| Potions | `$brewing_guide:potion_of_strength`, `…_swiftness`, `…_harming`, … | Brewing guide recipe book |

Brewing keys contain a colon (`$brewing_guide:…`). They are plain strings, so keep the prefix exactly as written.

## Adding an item

1. Find the item's numeric ID for your target Minecraft version.
2. Add a key in `_global_variables.json`: `"$<name>_item_id": <number>`.
3. Reference it from the screen as `$<name>_item_id` (for example in `item_id` on a smithing picker).
4. Validate and test. The validator only checks that the JSON is valid, not that the number is the right item.

## Known check items

Some numbers appear under two names. Each may be intentional. Confirm them in game:

| Number | Names |
|---|---|
| 347 | `$armor_items_tab_item_id`, `$iron_chestplate_item_id` |
| 351 | `$armor_preview_button_item_id`, `$diamond_chestplate_item_id` |
| 534 | `$mineral_items_tab_item_id`, `$nether_quartz_item_id` |
| 696 | `$smithing_template_tab_item_id`, `$netherite_upgrade_item_id` |

A repeated number is not an error on its own. It means a tab, button, and item share one ID.
If the wrong item appears, check these first.

## Note on IDs

The validator can't check numeric IDs against game data. Every ID here was taken from the original
upload and was not changed. If an item looks wrong in game, check its ID against the version's item list.
