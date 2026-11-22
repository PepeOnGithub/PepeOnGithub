# 02 — Folder structure

The pack is organized by **what a file is** (UI, textures, language) and then by **which feature it serves**.
Every folder name is lowercase with underscores. Every file is named after the thing it defines.

```
pack/
├── manifest.json                          pack identity (required to import)
├── font/
│   └── glyph_E0.png                       glyph font texture (the game requires font/ at the root)
├── texts/                                 translations: one .lang file per locale
│   ├── en_US.lang                         reference language (every key must be here)
│   └── ...                                27 other locales
├── textures/
│   ├── smithing_preview/                  every texture this pack adds, grouped by type
│   │   ├── buttons/                       toggle button states (default, hover, checked, checked hover)
│   │   ├── backgrounds/                   label and status backgrounds (nine-slice)
│   │   ├── icons/                         small icons: copper, drop, move, reset, row
│   │   ├── slots/                         slot and cell frames
│   │   └── brewing/
│   │       └── recipe_book/
│   │           ├── background.png         recipe book background
│   │           └── sprites/               tab, button, filter, and text-field sprites
│   │               └── bedrock/           Bedrock-style button sprites
└── ui/
    ├── _global_variables.json             shared $variables: item IDs and similar values
    ├── _ui_defs.json                      the list of custom files the game loads
    ├── <vanilla>_screen.json              overrides for vanilla screens (names must match vanilla)
    ├── smithing_table_2_screen.json       hooks the smithing table (vanilla name)
    ├── chest_screen.json                  hooks the chest (vanilla name)
    └── smithing_preview/                  everything this pack defines
        ├── shared/                        controls used by more than one screen
        │   ├── shared_controls.json       buttons, toggles, radio groups, input panels
        │   ├── item_movement.json         move and drop buttons for items
        │   ├── navigation.json            title bar, tabs, scroll areas
        │   └── management_toggles.json    reset, move, and drop toggles with status label
        ├── containers/                    chests
        │   ├── chest_single.json          1-row, 3-row, and hotbar layouts
        │   └── chest_double.json          6-row layout (built on chest_single)
        ├── smithing/                      smithing table
        │   ├── smithing_table.json        panels, item pickers, tab bar
        │   └── armor_arc.json             the armor arc and its slider
        ├── brewing/                       brewing stand guide
        │   ├── brewing_common.json        shared controls and text keys for the guide
        │   ├── brewing_factories.json     binds potion keys to their flags
        │   ├── brewing_toggles.json       tab and layout toggles
        │   ├── slots/
        │   │   ├── potion_slot.json       ingredient, result, and fuel slots + potion factories
        │   │   └── modifier_slot.json     duration and potency variants
        │   └── recipe_book/
        │       ├── recipe_book.json       recipe book panel and tabs
        │       └── recipe_grid.json       recipe grid
        └── compat/                        bridges and older files
            ├── container_item_bridge.json   connects brewing slots to the container item template
            └── legacy_container_item.json   older copy kept for reference (not loaded, see 21)
```

## Why this layout

- **One folder per feature.** To work on chests, you only open `containers/`.
- **Shared code lives in `shared/`.** Anything used by two or more screens goes there and nowhere else.
- **Textures mirror the UI.** Each texture lives under `textures/smithing_preview/` with a folder for its type.
  No texture is loose at the root of `textures/`. Vanilla textures are referenced by their vanilla paths and are not in this pack.
- **Vanilla names stay where the game expects them.** `ui/*_screen.json` files must keep their vanilla names,
  because the game matches them by name. Everything else is ours.

## Rules for new files

1. Put a new UI file in the folder for its feature. Use `shared/` only when two or more features use it.
2. Name the file after its namespace (see 03). `shared/navigation.json` defines the `sp_navigation` namespace.
3. Add the file to `ui/_ui_defs.json` if the game must load it.
4. Put a new texture under `textures/smithing_preview/` in the folder for its type. Never add loose textures.
