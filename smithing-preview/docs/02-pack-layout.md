# 02 — Pack layout

## Folder structure

```
pack/
├── manifest.json                      pack identity (added in this rework)
├── assets/brewing_guide/              source sprites referenced by path from brewing JSON
├── font/glyph_E0.png                  glyph font texture
├── texts/*.lang                       translations, 28 languages (en_US is the reference)
├── textures/
│   ├── ui/ashur/                      cell and slot textures
│   └── ui/pepe/
│       ├── buttons/                   toggle button textures
│       └── smithing/                  icons and label backgrounds for the smithing UI
└── ui/
    ├── _global_variables.json         shared $variables (item IDs, etc.)
    ├── _ui_defs.json                  the list of custom files the game loads
    ├── ui_common.json                 shared container / item renderer overrides (see 13)
    ├── <vanilla>_screen.json          overrides for vanilla screens (kept at ui/ root)
    └── pepe/
        ├── core/                      shared building blocks used by every screen
        │   ├── _global.json           redstone, search and toggle/radio/button mappings
        │   ├── item_data.json         item movement buttons (move / drop one, two, all)
        │   ├── toggle_manager.json    management toggles (reset, move, drop, status)
        │   └── uic.json               navigation tabs, scroll content, tab text panel
        ├── chests/
        │   ├── single_chest_content.json   1-row, 3-row and hotbar layouts
        │   └── double_chest_content.json   6-row layout, built on the single chest
        ├── smithing/
        │   ├── smithing.json          smithing table panels
        │   └── smithing_arc.json      armor-slot arc with rotation/slider states
        ├── compat/
        │   └── compatibility_container_item.json   brewing bridge (not in _ui_defs; see 13)
        └── brewing_guide/             brewing stand, recipe book and potion factories
            ├── brewing_global.json
            ├── brewing_toggle.json
            ├── factory_bindings.json
            ├── inventory_area/        potion slots and modifier slots
            └── recipe_book_area/      recipe book and its grid
```

## Old → new file map

The upload had a different layout. Only the files below moved. Their contents were not
changed, apart from the namespace renames and texture paths listed further down.

| Old path | New path |
|---|---|
| `ui/pepe/_global.json` | `ui/pepe/core/_global.json` |
| `ui/pepe/item_data.json` | `ui/pepe/core/item_data.json` |
| `ui/pepe/uic.json` | `ui/pepe/core/uic.json` |
| `ui/pepe/toggle_manager.json` | `ui/pepe/core/toggle_manager.json` |
| `ui/pepe/single_chest_content.json` | `ui/pepe/chests/single_chest_content.json` |
| `ui/pepe/double_chest_content.json` | `ui/pepe/chests/double_chest_content.json` |
| `ui/pepe/smithing.json` | `ui/pepe/smithing/smithing.json` |
| `ui/pepe/smithing_arc.json` | `ui/pepe/smithing/smithing_arc.json` |
| `ui/pepe/common/compatibility/advanced/compatibility_container_item.json` | `ui/pepe/compat/compatibility_container_item.json` |
| `textures/copper.png`, `drop.png`, `move.png`, `reset.png`, `row_icon.png`, `label_underlay.png`, `status_label_underlay.png` | `textures/ui/pepe/smithing/<same name>.png` |
| `textures/button_assets/*.png` | `textures/ui/pepe/buttons/*.png` |

Why the moves are safe: UI code refers to other files by **namespace** (for example
`smithing.lg_1e`), not by path. The only path-based references are `_ui_defs.json` and texture
strings, and both were updated and checked by the validator.

## Renamed namespaces

Three namespaces had machine-generated names. They were renamed everywhere they are used.

| Old | New | File |
|---|---|---|
| `bd-h1` | `smithing` | `pepe/smithing/smithing.json` |
| `f-ez18` | `smithing_arc` | `pepe/smithing/smithing_arc.json` |
| `es1e-` | `uic` | `pepe/core/uic.json` |

## Other changes

- Added `manifest.json`. The upload had none, so it could not be imported as a pack.
- The archive now has its files at the root. The old archive wrapped everything in a `Pepe/` folder.
- All JSON was reformatted to 2-space indentation, except for the two files listed in 13.
  Each reformat was checked to keep the parsed data identical.
- `_ui_defs.json` lists the same 15 files as before, grouped by role.
