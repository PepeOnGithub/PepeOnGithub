# Container guides

One guide per container, in the same shape as the brewing guide: what the screen is for, its tabs and contents,
the variables it uses, how this pack handles it today, and what to build next.

These guides follow the way the Glacier client pack builds its container screens. Glacier is a reference only.
Nothing in these guides copies its code, textures, or text. The item and enchantment lists come from the
structure Glacier uses, and are restated here as facts about the game.

## Status of each container in this pack

| Container | Guide | This pack today |
|---|---|---|
| Brewing stand | [05 — Brewing](05-brewing.md) | Full guide and recipe book (done) |
| Furnace, blast furnace, smoker | [01 — Furnace](01-furnace.md) | Management row only |
| Smithing table | [02 — Smithing](02-smithing.md) | Custom layout with three tabs, guide not built |
| Enchanting table | [03 — Enchanting](03-enchanting.md) | Management row only |
| Anvil | [04 — Anvil](04-anvil.md) | Management row only |
| Chest, double chest | [06 — Chest](06-chest.md) | Overlay rows, search and quick-transfer not built |
| Every container | [07 — Container anatomy](07-container-anatomy.md) | Shared parts described here |

## Guide anatomy (applies to every guide)

Every container guide is built from the same parts:

1. **Tab bar**: one tab per category (for example Foods, Ores, Blocks). A tab is a toggle with an icon.
2. **Item grid**: each tab shows its items in a grid. Each cell is a toggle with an item renderer.
3. **Detail text**: selecting an item shows its name, description, or max level in a text panel.
4. **Hover text**: moving over an item shows its name without opening it.
5. **Close and autoplace**: closing the screen can move items back to their place, as the container's own action.
6. **Layout toggle**: switches the guide panel open or closed.

The parts are shared through the container base (see [07](07-container-anatomy.md)).

## Building a guide for a new container

1. Read the container's guide template in [07](07-container-anatomy.md).
2. Pick the tab list: one tab per category, in the order a player needs them.
3. Put each item in exactly one tab. Use the item variable names from `_global_variables.json`.
4. Bind each tab's visibility to its toggle (`#visible` from the tab's `#toggle_state`).
5. Add detail text with `%lang` keys, so the guide translates.
6. Validate with `python3 tools/validate_pack.py pack`, then test in game (see the checklist at the end of each guide).
