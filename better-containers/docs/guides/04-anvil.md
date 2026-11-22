# 04 — Anvil guide

## Status

Built: `ui/better_containers/containers/anvil_guide.json`, hooked into the vanilla anvil after its management row. Four radio tabs: Repairable (12 groups, listed by item name), Formatting (the § codes), Colors (the 16 color codes), and Nametag. The Nametag tab reads its lines from `data/nametag_entries.json`. The file is empty: add one string per entry (what the nametag does), then re-run `tools/build_guides.py`.

The anvil guide is a reference, not a list of items for every task. It has four tabs: **Repairable Items**, **Formatting Codes**,
**Color Codes**, and **Nametag Easter Eggs**.

## Tabs

| Tab | Type | Contents |
|---|---|---|
| Repairable Items | item grid | 12 groups of items that the anvil can repair |
| Formatting Codes | text | Reference for `§` formatting codes |
| Color Codes | text | Reference for `§` color codes |
| Nametag Easter Eggs | text | Reference for special names that a nametag can carry. Check the exact behavior in game before you write it. |

### Repairable Items

**Repairable Items** (12)

`wooden_tools`, `shields`, `leather_armors`, `stone_tools`, `iron_tools`, `golden_tools`, `diamond_tools`, `netherite_tools`, `turtle_shell`, `elytra`, `mace`, `wolf_armor`


Each group is a set of items that the anvil repairs with the same material. Group names follow the game's
tool and armor categories.

## Mapping to this pack

The pack's anvil has only the management row. The repairable-items guide would be added as its own tab beside the vanilla anvil controls.

## What to build

1. The Repairable Items tab with the groups above.
2. Two text tabs for formatting and color codes, with one line per code.
3. The nametag reference as a text tab. Write its content for this pack; don't copy text from another pack.

## Checklist

- [ ] Repairable Items shows all twelve groups
- [ ] Formatting and color code tabs show their codes
- [ ] Each text tab scrolls on a small screen
