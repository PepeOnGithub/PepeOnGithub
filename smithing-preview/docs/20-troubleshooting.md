# 20 — Troubleshooting

## The pack doesn't show up or can't be imported

- `manifest.json` must be at the top level of the archive. The build script does this for you.
- Check the manifest fields: `format_version`, `header.uuid`, and `modules`.
- Delete the old copy of the pack from the device, then import again.

## The pack imports but nothing changes

- Check it's enabled on the world, under **Resource Packs** (not Behavior Packs).
- Check the Minecraft version. Vanilla control names change between updates.
- A file that isn't in `_ui_defs.json` may not load (see [21](21-known-issues-and-roadmap.md)).

## A vanilla screen is missing an element after a game update

- Start with the vanilla path in the hook. See [19](19-how-to-hook-a-vanilla-screen.md).
- The usual hooks are listed there. Compare each path with the vanilla UI for the new version.

## A control is missing, or a binding does nothing

- Check the name. The validator reports references that match no pack control, but it can't check bindings.
- Check that the namespace is right: `sp_` names are pack names. See [03](03-naming-conventions.md).
- If the old name shows up in your own notes, see [04 — Migration map](04-migration-map.md).

## A texture is missing or stretched

- Check that the path matches a real file under `textures/smithing_preview/` (the validator checks this).
- Check nine-slice and UV values against the image's real size (see [15](15-textures-and-fonts.md)).
- A vanilla texture that isn't in the pack can only be checked in game.

## A potion shows the wrong name or no name

- Check that its `%brewing.*` key exists in `texts/en_US.lang` (the validator checks this).
- Check its flag in `brewing_common.json` `text_keys`.
- Check its item ID in `_global_variables.json` (see [14](14-variables-and-item-ids.md)).

## Text is cut off

- Long translations overflow fixed-width panels. Shorten the string or widen the panel.
- Some languages are much longer than English. Test them in game.

## The validator reports an ERROR about a retired namespace

- A file still uses an old namespace name (for example `single_chest_content`). Replace it with the new name from [04](04-migration-map.md).

## The build fails with "validation failed"

- Read the `ERROR` lines above the message. The build won't run until they're fixed.
