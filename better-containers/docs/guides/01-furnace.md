# 01 — Furnace guide

The furnace guide shows what can be smelted, and what burns as fuel. It covers the three furnace screens: the **furnace**,
the **blast furnace** (ores), and the **smoker** (food). In the reference structure, one file serves all three, and
two conditions hide the tabs that don't apply.

## What the screen does

- Input slot, fuel slot, and output slot (vanilla)
- Progress arrows: a flame bar for fuel and an arrow bar for smelting, each with a percentage
- A time readout for the remaining smelt time

## Tabs

| Tab | Items | Furnace | Blast furnace | Smoker |
|---|---|---|---|---|
| Foods | 9 | yes | no (label hidden) | yes |
| Ores | 14 | yes | yes | no (label hidden) |
| Blocks | 16 | yes | yes | yes |
| Nature | 10 | yes | yes | yes |
| Fuel | 32 | yes | yes | yes |

The **Foods** label is hidden on the blast furnace, and the **Ores** label is hidden on the smoker. Each hide is an `ignored` condition on the tab label, using `$is_blast_furnace` and `$is_smoker`. The reference file hides the label; check in game whether the tab button also needs hiding.

### Items in each tab

**Foods** (9)

`raw_beef`, `raw_porkchop`, `raw_chicken`, `raw_mutton`, `raw_rabbit`, `raw_cod`, `raw_salmon`, `potato`, `kelp`

**Ores** (14)

`raw_iron`, `raw_copper`, `raw_gold`, `nether_gold_ore`, `ancient_debris`, `redstone_ore`, `coal_ore`, `emerald_ore`, `lapis_lazuli_ore`, `diamond_ore`, `nether_quartz_ore`, `iron_ore`, `copper_ore`, `gold_ore`

**Blocks** (16)

`cobblestone`, `stone`, `stone_bricks`, `cobbled_deepslate`, `deepslate_bricks`, `deepslate_tiles`, `sandstone`, `red_sandstone`, `nether_bricks`, `basalt`, `polished_blackstone_bricks`, `block_of_quartz`, `clay`, `dyed_terracotta`, `sand`, `wet_sponge`

**Nature** (10)

`log`, `wood`, `chorus_fruit`, `sea_pickle`, `cactus`, `clay_ball`, `netherrack`, `iron_tools`, `gold_tools`, `leaves`

**Fuel** (32)

`lava_bucket`, `block_of_coal`, `dried_kelp_block`, `blaze_rod`, `coal`, `charcoal`, `boat`, `bamboo_blocks`, `bee_nest`, `beehive`, `chiseled_bookshelf`, `log`, `wood`, `wooden_building_blocks`, `utility_blocks`, `fishing_rod`, `crossbow`, `bow`, `wooden_door`, `sign`, `hanging_sign`, `wooden_tools`, `bowl`, `saplings`, `stick`, `dead_bush`, `azalea`, `leaf_litter`, `short_dry_grass`, `tall_dry_grass`, `bamboo`, `scaffolding`


## Variables

| Variable | Meaning |
|---|---|
| `$is_blast_furnace` | Hides the Foods tab |
| `$is_smoker` | Hides the Ores tab |
| `$is_left_most_tab`, `$is_right_most_tab` | Tab edge styling |
| `$item_id` | Item shown by a tab cell |
| `$button_text` | Lang key for the item name |

## How this pack handles it today

The pack has no furnace layout. It adds only the management row (see [containers 08](../containers/08-furnace.md)).

## What to build

1. One guide file that serves the furnace, blast furnace, and smoker, with the two `ignored` conditions.
2. Five tabs with the lists above. Start with Foods and Fuel, because they're the most used.
3. The flame and arrow progress bars, using the furnace's `$*_percentage` templates.
4. A test for each of the three screens.

## Checklist

- [ ] Furnace: five tabs show, and each lists its items
- [ ] Blast furnace: no Foods tab, ore tabs show
- [ ] Smoker: no Ores tab, food tab shows
- [ ] Clicking an item shows its name in the detail text
- [ ] Flame and arrow bars move during smelting
