# 09 — Textures, fonts and assets

## Where things live

| Folder | Contents |
|---|---|
| `textures/ui/pepe/buttons/` | Toggle button states: `toggle_default`, `toggle_hover`, `toggle_checked`, `toggle_checked_hover` |
| `textures/ui/pepe/smithing/` | Smithing icons and labels: `copper`, `drop`, `move`, `reset`, `row_icon`, `label_underlay`, `status_label_underlay` |
| `textures/ui/ashur/` | Slot and cell textures (`white_slot`, `cell_*`) |
| `assets/brewing_guide/` | Brewing sprites: the recipe book background and tab/button sprites |
| `font/glyph_E0.png` | Glyph font texture (the `E0` range used for a custom glyph) |

## Path rules

- Write texture paths as the game sees them, starting with `textures/` and without the `.png`
  extension (the game adds it). Example: `"textures/ui/pepe/smithing/drop"`.
- The brewing guide uses `assets/...` paths. Those paths are relative to the pack root, so the
  files must stay in `assets/`. Don't move them under `textures/`.
- Paths are plain strings. Renaming a file means finding every reference, which is why the validator checks them.

## Vanilla textures

Some UI refers to vanilla textures (for example `textures/ui/TabTopBack`, `textures/ui/White`).
They are **not** shipped in this pack and are supplied by the game. The validator reports them as a
single warning. They can't be checked offline, so confirm them in game after a Minecraft update.

## Nine-slice and sizes

Many controls use `$*_nineslice` values and `$*_uv` / `$*_uv_size` for sprite sheets. These
settings must match the texture's real size. A wrong size is the most common cause of stretched or
clipped images.

## Adding a texture

1. Save the PNG in the folder that matches its role (see the table above).
2. Reference it as `textures/<folder>/<name>` in the UI file or in a `$variable`.
3. Run the validator. It fails if the file is missing.
4. Check the image in game at the scale the UI uses.
