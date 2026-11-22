# 01 — Getting started

## What you need

- Minecraft Bedrock Edition, on a version that supports JSON UI resource packs.
- Python 3.9 or newer for the tools. They use only the standard library.
- Basic JSON knowledge. Bedrock UI JSON also accepts `//` and `/* */` comments.

## Install the pack

1. From the repository root, run:
   ```bash
   python3 tools/build_mcpack.py
   ```
   This validates `pack/` and writes `dist/Better-Containers.mcpack`.
2. Open the `.mcpack` on your device to import it.
3. Edit a world, open **Resource Packs**, and activate **Better Containers**.
4. Load the world and open a smithing table, a chest, a double chest, and a brewing stand.

## The edit loop

1. Change a file under `pack/`.
2. Run `python3 tools/validate_pack.py pack`. Fix every `ERROR` before you test.
3. Rebuild and re-import. Minecraft caches packs, so delete the old copy on the device first if you don't see your change.
4. Test in game. The validator checks structure and references, not how the UI looks.

## Where to go next

| I want to... | Read |
|---|---|
| Understand the folder layout | [02 — Folder structure](02-folder-structure.md) |
| Name a new file, control, or texture correctly | [03 — Naming conventions](03-naming-conventions.md) |
| Find an old name from the previous version | [04 — Migration map](04-migration-map.md) |
| Learn the JSON UI mechanics used here | [05 — JSON UI concepts](05-json-ui-concepts.md) |
| Reuse an existing template | [06 — Template catalog](06-template-catalog.md) |
| Change the smithing table | [07 — Smithing table](07-smithing-table.md) |
| Change the armor arc | [08 — Armor arc](08-armor-arc.md) |
| Change chests | [09 — Chests](containers/01-chest.md) |
| Change shared buttons, tabs, and toggles | [10 — Shared controls](10-shared-controls.md) |
| Work on the brewing stand | [11 — Brewing guide overview](11-brewing-guide-overview.md) |
