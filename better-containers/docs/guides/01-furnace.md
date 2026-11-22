# 01 — Furnace guide

The furnace guide is the in-game panel beside the furnace. It lists what can be smelted, what can be smoked, and what burns as fuel.
It covers the **furnace**, the **blast furnace**, and the **smoker**. It's the first container guide built in code.

## Status

| Part | State |
|---|---|
| Panel and five tabs | Built: `ui/better_containers/containers/furnace_guide.json` |
| Item cells | Built: shared `ui/better_containers/shared/item_cell.json` |
| Hook into the vanilla furnace | Built: `ui/furnace_screen.json` (after the management row) |
| Blast furnace and smoker | Built: `ui/blast_furnace_screen.json` sets `$is_blast_furnace`, `ui/smoker_screen.json` sets `$is_smoker`; each places the guide. Not verified in game (see below) |
| Progress bars (fuel and smelting) | Built: two bars bound to `#furnace_flame_ratio` and `#furnace_arrow_ratio`, the vanilla globals the reference uses. Verify the bar widths in game |
| Smelt time text | Built as fixed text (10 s furnace, 5 s blast furnace and smoker), and each fuel shows its burn time. These are the vanilla values, not live readings |
| Hover detail text | Not built |

## Tabs

| Tab | Items | Items (in order) |
|---|---|---|
| Foods | 9 | `beef`, `porkchop`, `chicken`, `mutton`, `rabbit`, `cod`, `salmon`, `potato`, `kelp` |
| Ores | 14 | `coal_ore`, `copper_ore`, `diamond_ore`, `emerald_ore`, `gold_ore`, `iron_ore`, `lapis_ore`, `nether_gold_ore`, `quartz_ore`, `redstone_ore`, `ancient_debris`, `raw_copper`, `raw_gold`, `raw_iron` |
| Blocks | 9 | `cobblestone`, `sand`, `clay`, `netherrack`, `basalt`, `cobbled_deepslate`, `stone_bricks`, `deepslate_bricks`, `deepslate_tiles` |
| Nature | 5 | `cactus`, `chorus_fruit`, `sea_pickle`, `clay_ball`, `oak_log` |
| Fuel | 9 | `coal`, `charcoal`, `coal_block`, `blaze_rod`, `lava_bucket`, `dried_kelp_block`, `bamboo`, `bamboo_block`, `stick` |

Each tab is a radio toggle (`bc_shared.radio`). Selecting a tab shows its items, through a `#visible` binding on the tab's toggle.

## Why these lists differ from the reference

The reference pack's furnace tabs include entries that aren't furnace inputs or fuel (for example `bow`, `crossbow`), plus
group headings such as "Wooden Building Blocks". Those can't be correct in a furnace guide, so this guide uses a curated list:
every item is a real smelting input, smoking input, or fuel in vanilla. Group names (`log`, `wood`, `iron_tools`) were left out
because they cover several items, and an item must be a single entry to be shown.

Before you ship, check each item in game: put it in the furnace and confirm it smelts, smokes, or burns.

## Variables

| Variable | Set by | Meaning |
|---|---|---|
| `$is_blast_furnace` | the vanilla screen (default `false`) | Hides the Foods label and tab |
| `$is_smoker` | the vanilla screen (default `false`) | Hides the Ores label and tab |
| `$<item>_item_id` | `_global_variables.json` | Item ID for each cell |

The `$is_blast_furnace` and `$is_smoker` values are set on the blast furnace and smoker screen roots by the override files. The guide hides the Foods tab on the blast furnace and the Ores tab on the smoker. The override mechanism follows the reference pack; check it in game first.

## Item IDs

Every item ID comes from `data/item_ids/stable-1.26.60.json`, the same list the Minecraft Item ID Viewer uses. Run
`python3 tools/sync_item_ids.py` to check them against that list. Re-run `python3 tools/build_guides.py` after you change a tab.

## Build steps (what the generator does)

1. Writes the shared item cell and the furnace guide file.
2. Adds any missing `$<item>_item_id` to `_global_variables.json`. It never overwrites a value, and stops if a value differs.
3. Registers both UI files in `_ui_defs.json`, which the game needs to load them.
4. Adds the guide's strings to every language file.
5. Adds the guide to the furnace hook.

## Checklist

- [ ] Furnace: five tabs show, with the listed items
- [ ] Clicking a tab shows only its items
- [ ] Blast furnace: no Foods tab (verify)
- [ ] Smoker: no Ores tab (verify)
- [ ] Each curated item smelts, smokes, or burns as the tab says
- [ ] The guide doesn't cover the management row or the vanilla slots

## Wiki check

`data/wiki/furnace.json` holds the full Bedrock smelting and fuel lists from the Minecraft Wiki (245 fuels, 111 smeltable items the guide does not show, such as gear that smelts to nuggets and all terracotta). The guide tabs now include deepslate ores, more stone blocks, resin clump and every log type. Nothing in the old lists was wrong.
