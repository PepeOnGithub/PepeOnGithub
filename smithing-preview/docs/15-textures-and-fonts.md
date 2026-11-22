# 15 — Textures and fonts

## The texture tree

Every texture this pack adds lives under `textures/smithing_preview/`, in a folder for its type.

| Folder | Contents |
|---|---|
| `buttons/` | Toggle button states: `toggle_default`, `toggle_hover`, `toggle_checked`, `toggle_checked_hover` |
| `backgrounds/` | Nine-slice backgrounds for labels: `label_underlay`, `status_label_underlay` |
| `icons/` | Small icons: `copper`, `drop`, `move`, `reset`, `row_icon` |
| `slots/` | Slot and cell frames: `white_slot`, `cell_white`, `cell_red_transparent`, `cell_focus_unselect` |
| `brewing/recipe_book/` | `background.png`, the recipe book background |
| `brewing/recipe_book/sprites/` | Tab, button, filter, slot, and text-field sprites |
| `brewing/recipe_book/sprites/bedrock/` | Bedrock-style button sprites |

Font files stay in `font/` because the game expects them there: `font/glyph_E0.png` is the glyph font texture.

## Path rules

- Write paths as the game sees them: start with `textures/`, and leave out the `.png` extension. Example:
  `"textures/smithing_preview/icons/drop"`.
- Paths are strings. Renaming a file means changing every reference. The validator fails if a pack path doesn't resolve.
- Put a new texture in the folder for its type. Don't add loose files at the root of `textures/`.

## Vanilla textures

Some UI refers to vanilla textures, for example `textures/ui/TabTopBack`, `textures/ui/White`, and `textures/ui/recipe_book_icon`.
They aren't shipped in this pack. The validator reports them as one warning. Check them in game after a Minecraft update.

## Nine-slice and sizes

Controls use `$*_nineslice` values and `$*_uv` / `$*_uv_size` for sprite sheets. Those values must match the
texture's real size. A wrong size causes stretched or clipped images, which is the most common texture problem.

## Adding a texture

1. Save the PNG in the folder for its type.
2. Reference it as `textures/smithing_preview/<folder>/<name>` in the UI file, or in a `$variable`.
3. Run the validator. It fails if the file is missing.
4. Check it in game at the size the UI uses.
