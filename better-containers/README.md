# Better Containers — JSON UI resource pack

A Minecraft Bedrock resource pack that restyles the **smithing table**, the **chest and double chest**, and the
**brewing stand**, with a brewing guide and recipe book.

## Repository layout

```
better-containers/
├── pack/          resource pack source (the folder that gets zipped)
│   ├── manifest.json
│   ├── font/
│   ├── texts/             translations (28 locales)
│   ├── textures/better_containers/   every texture this pack adds, by type
│   └── ui/
│       ├── _global_variables.json, _ui_defs.json
│       ├── <vanilla>_screen.json    vanilla hooks (names must match the game)
│       └── better_containers/        everything this pack defines, by feature
├── docs/          guides (start at 01)
├── tools/
│   ├── validate_pack.py   checks JSON, references, textures, language keys
│   └── build_mcpack.py    validates, then zips pack/ into dist/*.mcpack
└── dist/          built packs (not committed)
```

## Quick start

```bash
python3 tools/validate_pack.py pack        # must report "0 error(s)"
python3 tools/build_mcpack.py              # writes dist/Better-Containers.mcpack
```

Import the `.mcpack` on your device, enable it under **Resource Packs** on a world, then test the smithing table,
chests, the brewing stand, and the recipe book.

## Guides

| # | Guide | Covers |
|---|---|---|
| 01 | [Getting started](docs/01-getting-started.md) | Install, build, and the edit loop |
| 02 | [Folder structure](docs/02-folder-structure.md) | Where every file and texture lives, and why |
| 03 | [Naming conventions](docs/03-naming-conventions.md) | Namespaces, controls, variables, files, and textures |
| 04 | [Migration map](docs/04-migration-map.md) | Every old name → new name, from the original upload |
| 05 | [JSON UI concepts](docs/05-json-ui-concepts.md) | Namespaces, templates, variables, bindings, modifications |
| 06 | [Template catalog](docs/06-template-catalog.md) | Main templates and a generated index of every control |
| 07 | [Smithing table](docs/07-smithing-table.md) | The smithing screen, its hook, and its controls |
| 08 | [Armor arc](docs/08-armor-arc.md) | The two arcs, their slots, and the slider |
| 09 | [Containers](docs/containers/README.md) | Every vanilla container the pack changes, one guide each (14 guides) |
| 10 | [Shared controls](docs/10-shared-controls.md) | Buttons, toggles, tabs, move and drop buttons |
| 11 | [Brewing guide overview](docs/11-brewing-guide-overview.md) | How the brewing guide is put together |
| 12 | [Potions and factories](docs/12-brewing-factories-and-potions.md) | Potion factories, flags, and their bindings |
| 13 | [Recipe book](docs/13-brewing-recipe-book.md) | Recipe book, grid, tabs, and layout |
| 14 | [Variables and item IDs](docs/14-variables-and-item-ids.md) | `_global_variables.json` and how to add an item |
| 15 | [Textures and fonts](docs/15-textures-and-fonts.md) | The texture tree, path rules, nine-slice, and fonts |
| 16 | [Localization](docs/16-localization.md) | Language files, key parity, adding a language |
| 17 | [Validation and building](docs/17-validation-and-building.md) | What the validator checks and how to read its output |
| 18 | [How to add a potion](docs/18-how-to-add-a-potion.md) | Step-by-step checklist |
| 19 | [How to hook a vanilla screen](docs/19-how-to-hook-a-vanilla-screen.md) | Vanilla hooks, with examples and the existing ones |
| 20 | [Troubleshooting](docs/20-troubleshooting.md) | Common problems and fixes |
| 21 | [Known issues and roadmap](docs/21-known-issues-and-roadmap.md) | What changed, what didn't, and next steps |
| 22 | [Glossary](docs/22-glossary.md) | Definitions of the terms used in these guides |

## Status

- Verified by the validator: 0 errors. It checks structure and references, not visuals.
- The renames preserve every reference. They have not yet been checked in Minecraft.
  Start with [21 — Known issues](docs/21-known-issues-and-roadmap.md).
