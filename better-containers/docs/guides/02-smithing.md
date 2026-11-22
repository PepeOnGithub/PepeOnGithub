# 02 — Smithing table guide

## Status

Built: `ui/better_containers/containers/smithing_guide.json`, hooked into the vanilla smithing table after its management row. Three radio tabs (Armors 25, Smithing Templates 19, Resources 11), using the item variables. Verify in game: the panel's position beside the pack's own smithing layout, which the hook does not measure.

The smithing guide shows which items can be upgraded, which templates apply, and which resources they need.
It's the closest container to the pack's own smithing table (see [07 — Smithing table](../07-smithing-table.md)).

## Tabs

| Tab | Items | First items |
|---|---|---|
| Armors | 25 | `leather_helmet`, `leather_chestplate`, `leather_leggings`, `leather_boots`, `chainmail_helmet` |
| Smithing Templates | 19 | `netherite_upgrade`, `sentry_trim`, `vex_trim`, `wild_trim`, `coast_trim` |
| Resources | 11 | `amethyst_shard`, `copper_ingot`, `diamond`, `emerald`, `gold_ingot` |

### Items in each tab

**Armors** (25)

`leather_helmet`, `leather_chestplate`, `leather_leggings`, `leather_boots`, `chainmail_helmet`, `chainmail_chestplate`, `chainmail_leggings`, `chainmail_boots`, `iron_helmet`, `iron_chestplate`, `iron_leggings`, `iron_boots`, `golden_helmet`, `golden_chestplate`, `golden_leggings`, `golden_boots`, `diamond_helmet`, `diamond_chestplate`, `diamond_leggings`, `diamond_boots`, `netherite_helmet`, `netherite_chestplate`, `netherite_leggings`, `netherite_boots`, `turtle_shell`

**Smithing Templates** (19)

`netherite_upgrade`, `sentry_trim`, `vex_trim`, `wild_trim`, `coast_trim`, `dune_trim`, `wayfinder_trim`, `shaper_trim`, `raiser_trim`, `host_trim`, `ward_trim`, `silence_trim`, `tide_trim`, `snout_trim`, `rib_trim`, `eye_trim`, `spire_trim`, `flow_trim`, `bolt_trim`

**Resources** (11)

`amethyst_shard`, `copper_ingot`, `diamond`, `emerald`, `gold_ingot`, `iron_ingot`, `lapis_lazuli`, `nether_quartz`, `netherite_ingot`, `redstone_dust`, `resin_brick`


## Mapping to this pack

| Reference tab | This pack's control |
|---|---|
| Armors | `armor_tab_icon` (uses the armor item ID) |
| Smithing Templates | `template_tab_icon` |
| Resources | `mineral_tab_icon` (this pack calls it Minerals) |

The pack's armor arc ([08](../08-armor-arc.md)) is its own design, and it has no direct equivalent in the reference tabs.

## Recipe button

The reference smithing table has a recipe button that opens the guide panel. The pack's smithing table has no recipe button yet.

## What to build

1. Three tabs with the lists above, using the item IDs from `_global_variables.json`.
2. Smithing templates: one cell per trim and the netherite upgrade.
3. A recipe button and a guide panel with its own text.

## Checklist

- [ ] Three tabs show, and the Armors tab lists all four armor sets
- [ ] Each template shows its trim name on hover
- [ ] Resources tab lists the upgrade materials
- [ ] The recipe button opens and closes the guide panel
