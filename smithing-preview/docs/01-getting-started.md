# 01 — Getting started

## What you need

- Minecraft Bedrock Edition (a version that supports JSON UI resource packs).
- Python 3.9+ for the tools (no third-party packages).
- Basic JSON knowledge. Bedrock UI JSON also accepts `//` and `/* */` comments.

## Install the pack

1. Run `python3 tools/build_mcpack.py`. This creates `dist/Smithing-Preview.mcpack`.
2. Open the `.mcpack` file on the device with Minecraft to import it.
3. Edit a world, go to **Resource Packs**, and activate *Smithing Preview*.
4. Load the world and open a smithing table, chest, or brewing stand to check.

## Edit workflow

1. Change a file under `pack/`.
2. Run `python3 tools/validate_pack.py pack`. Fix every error before testing.
3. Rebuild and re-import. Minecraft caches packs, so if you don't see a change,
   delete the old copy of the pack from the device and import it again.
4. Test in game. The validator can't render UI.

## Where to start reading

- Want to know how the files fit together? Read [03 — JSON UI concepts](03-json-ui-concepts.md).
- Want to change the smithing table? Start with [04](04-smithing-screen.md).
- Want to change potion or ingredient behavior? Start with [08](08-variables-and-item-ids.md)
  and [07](07-brewing-guide.md).
- Want to add a translation? See [10](10-localization.md).
