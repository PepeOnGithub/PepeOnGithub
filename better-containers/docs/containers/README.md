# Containers

Every vanilla container the pack changes has its own guide. Each guide follows the same layout, so you can find the
same information for any container.

## How container overrides work

A vanilla screen is a JSON file at the root of `ui/` with a name the game recognizes (for example `anvil_screen.json`).
The pack adds a file with the same name, and that file uses `modifications` to add or remove controls in the vanilla layout.

There are two patterns:

| Pattern | What it does | Containers |
|---|---|---|
| **Management row** | Inserts `bc_management_toggles.primary_management_toggles` (reset, move, drop) on the right | Anvil, beacon, cartography, enchanting, furnace, grindstone, horse, inventory, loom, trade, smithing table |
| **Custom layout** | Replaces or adds whole panels | Chest, smithing table, brewing stand |
| **Shared content** | Inserts `bc_shared.redstone_content` (a row and a search box) | Redstone |

Vanilla overrides are not listed in `_ui_defs.json`. The game applies them by their vanilla file names, which is why they stay at the root of `ui/`.

## Index

| # | Container | Pattern | Guide |
|---|---|---|---|
| 01 | Chest (single and double) | Custom layout (overlays) | [01-chest.md](01-chest.md) |
| 02 | Smithing table | Custom layout (replaces root) | [02-smithing-table.md](02-smithing-table.md) |
| 03 | Brewing stand | Custom layout (guide and recipe book) | [03-brewing-stand.md](03-brewing-stand.md) |
| 04 | Anvil | Management row | [04-anvil.md](04-anvil.md) |
| 05 | Beacon | Management row | [05-beacon.md](05-beacon.md) |
| 06 | Cartography table | Management row | [06-cartography.md](06-cartography.md) |
| 07 | Enchanting table | Management row | [07-enchanting.md](07-enchanting.md) |
| 08 | Furnace | Management row | [08-furnace.md](08-furnace.md) |
| 09 | Grindstone | Management row | [09-grindstone.md](09-grindstone.md) |
| 10 | Horse, donkey, and mule | Management row (root panel) | [10-horse.md](10-horse.md) |
| 11 | Player inventory | Management row | [11-inventory.md](11-inventory.md) |
| 12 | Loom | Management row | [12-loom.md](12-loom.md) |
| 13 | Redstone (plain and crafter) | Shared content | [13-redstone.md](13-redstone.md) |
| 14 | Villager trading | Management row | [14-trade.md](14-trade.md) |

## Adding a new container

1. Find the vanilla screen's file name and the path to its inventory panel. Use the vanilla UI for the game version you target.
2. Create `ui/<screen>_screen.json` at the root of `ui/` with the name the game expects.
3. Pick a pattern from the table above. For the management row, copy an existing hook (for example `anvil_screen.json`) and change the path.
4. Add a guide here: copy an existing one, change the table, and list the testing steps for that screen.
5. Run `python3 tools/validate_pack.py pack`, then test the screen in game.

## Rules every container guide follows

- The hook path, operation, and inserted control are listed in the "At a glance" table.
- Each guide says what the pack adds, and what it leaves alone.
- Each guide ends with a testing checklist and known limitations.
