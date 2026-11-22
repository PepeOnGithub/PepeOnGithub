# 12 — Troubleshooting

## The pack doesn't show up or can't be imported

- Make sure `manifest.json` is at the top level of the archive (it is, if you used `build_mcpack.py`).
- Check that the `format_version`, `header.uuid`, and `module` fields are present and valid.
- Re-import: delete the old copy of the pack from the device first.

## The pack imports but nothing changes in game

- Check it's **enabled** on the world (Resource Packs, not just Behavior Packs).
- Check the Minecraft version. Vanilla control names change between updates.
- A file not listed in `ui/_ui_defs.json` may not be loaded (see 13).

## A vanilla screen is missing an element after a game update

- Vanilla path hooks are the usual cause. Check these:
  - `smithing_table_2_screen.json` → `smithing_table_panel/root_panel/smithing_table_screen_inventory`
  - `chest_screen.json` → `small_chest_panel/root_panel/chest_panel`, `large_chest_panel/root_panel/chest_panel`
  - `anvil_screen.json`, `beacon_screen.json` → their `*_inventory` paths
- Compare the vanilla control name with the one in the override, and update the path.

## A texture is missing or stretched

- Confirm the path matches a real file in `textures/` (the validator checks this for pack textures).
- Check the nine-slice and UV values against the image's real size (see 09).
- A `textures/ui/...` vanilla texture that isn't in the pack can only be checked in game.

## A brewing potion shows the wrong name or no name

- Check its `%brewing.*` key exists in `texts/en_US.lang` (the validator checks this).
- Check its key is in `brewing_global.json` `text_keys`.
- Check the item ID in `_global_variables.json` (see 08).

## Text is cut off

- Long translations overflow fixed-width panels. Shorten the string or widen the panel.
- Check the language in game: some languages are much longer than English.

## Validator reports a `@` reference warning I don't understand

- Warnings for `@`-references are usually vanilla namespaces with the same name as a pack namespace (for example `_global`).
  Test in game before changing anything.

## Build fails with "validation failed"

- Read the `ERROR` lines above the message. The build won't run until they're fixed.
