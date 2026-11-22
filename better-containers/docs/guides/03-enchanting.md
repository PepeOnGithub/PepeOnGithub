# 03 — Enchanting guide

## Status

Built: `ui/better_containers/containers/enchanting_guide.json`, hooked into the vanilla enchanting screen. It is a scrolling list of all 41 enchantments, one row each, with the enchanted book icon, the vanilla enchantment name, and its max level. Not built: selecting a row to show a description (the reference shows descriptions; this pack doesn't copy that text), and the level text is in English only.

The enchanting guide is a book of enchantments. It has one tab, **Enchanted Books**, with one cell per enchantment.
Selecting a cell shows the enchantment's description and max level.

## Structure

| Part | Source | Role |
|---|---|---|
| Enchanted Books tab | the book item (`enchanted_book`) | The single tab |
| Enchantment cell | a toggle with the name key (`$button_text`) | One enchantment |
| Description | `$description_text` | What the enchantment does |
| Max level | `$level_text` | Shown as `Max Level: <roman numeral>` |

The max level text is `§7Max Level: ` followed by the level, so the color code is part of the text.

## Enchantments and max levels

The table lists each enchantment in the reference data, with its lang key and the max level shown there.
Each name key is a vanilla lang key, so the name translates with the game's language.

| Lang key | Max level |
|---|---|
| `enchantment.arrowDamage` | V (5) |
| `enchantment.arrowFire` | I (1) |
| `enchantment.arrowInfinite` | I (1) |
| `enchantment.arrowKnockback` | II (2) |
| `enchantment.crossbowMultishot` | I (1) |
| `enchantment.crossbowPiercing` | IV (4) |
| `enchantment.crossbowQuickCharge` | III (3) |
| `enchantment.curse.binding` | I (1) |
| `enchantment.curse.vanishing` | I (1) |
| `enchantment.damage.all` | V (5) |
| `enchantment.damage.arthropods` | V (5) |
| `enchantment.damage.undead` | V (5) |
| `enchantment.digging` | V (5) |
| `enchantment.durability` | III (3) |
| `enchantment.fire` | II (2) |
| `enchantment.fishingSpeed` | III (3) |
| `enchantment.frostWalker` | II (2) |
| `enchantment.heavy_weapon.breach` | IV (4) |
| `enchantment.heavy_weapon.density` | V (5) |
| `enchantment.heavy_weapon.windBurst` | III (3) |
| `enchantment.knockback` | II (2) |
| `enchantment.lootBonus` | III (3) |
| `enchantment.lootBonusDigger` | III (3) |
| `enchantment.lootBonusFishing` | III (3) |
| `enchantment.mending` | I (1) |
| `enchantment.oxygen` | III (3) |
| `enchantment.protect.all` | IV (4) |
| `enchantment.protect.explosion` | IV (4) |
| `enchantment.protect.fall` | IV (4) |
| `enchantment.protect.fire` | IV (4) |
| `enchantment.protect.projectile` | IV (4) |
| `enchantment.soul_speed` | III (3) |
| `enchantment.swift_sneak` | III (3) |
| `enchantment.thorns` | III (3) |
| `enchantment.tridentChanneling` | I (1) |
| `enchantment.tridentImpaling` | V (5) |
| `enchantment.tridentLoyalty` | III (3) |
| `enchantment.tridentRiptide` | III (3) |
| `enchantment.untouching` | I (1) |
| `enchantment.waterWalker` | III (3) |
| `enchantment.waterWorker` | I (1) |

## How this pack handles it today

The pack has no enchanting layout. It adds only the management row (see [containers 07](../containers/07-enchanting.md)).

## What to build

1. The Enchanted Books tab, with one toggle cell per enchantment in the table.
2. A description panel that shows the name, description, and `Max Level` line.
3. Descriptions written for this pack, in `texts/`, with `%lang` keys (do not copy another pack's text).

## Checklist

- [ ] The Enchanted Books tab shows every enchantment in the table
- [ ] Each cell shows its name on hover
- [ ] Selecting a cell shows its description and max level
- [ ] The max level matches the table for three sample enchantments
