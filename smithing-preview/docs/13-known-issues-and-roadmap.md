# 13 — Known issues and roadmap

This guide lists what the rework changed, what it deliberately didn't change, and what still needs work.

## What this rework did

- Moved files into `core/`, `chests/`, `smithing/`, `compat/`, and grouped the textures (see 02).
- Renamed three generated namespaces (`bd-h1`, `f-ez18`, `es1e-`) to readable names.
- Reformatted JSON to 2-space indentation. Each reformat was checked to keep the parsed data identical.
- Added `manifest.json` (the upload had none).
- Moved the archive contents to the root (the upload wrapped them in a `Pepe/` folder).
- Added the validator and build script, and wrote these guides.

## What it did **not** change

The UI logic was **not rewritten**. The pack is about 160 KB of interdependent JSON with machine-generated
control names. A rewrite without being able to run Minecraft would very likely break it. The
safe changes above are verified by the validator, which checks structure and references. Gameplay and visuals
are intended to be unchanged, but **that still needs to be confirmed in game**.

## Open issues

### 1. Duplicate key in `ui/ui_common.json`

`container_item` appears twice at the top level. JSON parsers keep only one of the two values, and
the game may keep either. This file was not reformatted, so the duplicate is intact.

- Decide which definition is meant to win, then merge the two into one key.
- The two definitions overlap with `ui/pepe/compat/compatibility_container_item.json`. Keep one source of truth.

### 2. `compatibility_container_item.json` isn't in `_ui_defs.json`

The file is in the pack but not listed. It was unlisted in the upload too, so its behavior is unchanged.
Test in game with and without it listed, then add it if it's meant to load.

### 3. Machine-generated control names remain

Most control names inside `smithing/`, `core/uic.json`, and the brewing files are still generated IDs
(for example `l_0oe`, `gho_66`, `dl_s72`). They are referenced from many places, so renaming them needs
a careful, scripted pass. Do it one file at a time, and run the validator after each file.

### 4. Vanilla textures and paths can't be checked offline

24 vanilla texture paths and the vanilla screen hooks depend on the game version. Re-check them after
each Minecraft update.

### 5. Missing metadata

- No `pack_icon.png`, so the pack shows without an icon.
- No `min_engine_version` in the manifest. Set it to the lowest version you have tested.
- The manifest UUIDs were generated from fixed names, so they're stable across builds. If you publish
  this pack alongside another one, give it its own UUIDs.

### 6. Numeric item IDs

Item IDs in `_global_variables.json` were not verified against game data. Some numbers are reused on
purpose (see 08). Check the important ones in game.

## Roadmap (suggested order)

1. Test the reorganized pack in game on each screen (smithing, chest, double chest, brewing stand, recipe book).
2. Fix open issue 1 (the duplicate key), then decide on issue 2.
3. Rename control IDs file by file, starting with `core/uic.json` (smallest), then `core/toggle_manager.json`.
4. Add a `pack_icon.png` and `min_engine_version`.
5. Add an automated check that runs the game's UI loader, if one becomes available.
