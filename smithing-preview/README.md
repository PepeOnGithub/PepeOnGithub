# Smithing Preview — JSON UI resource pack

A Minecraft Bedrock resource pack that reworks the **smithing table**, **chest / double chest**,
and **brewing stand** (with a brewing guide and recipe book) interfaces.

This repository holds the pack source in `pack/`, the guides in `docs/`, and the
tools in `tools/`.

```
smithing-preview/
├── pack/          ← resource pack source (this folder is what gets zipped)
├── docs/          ← guides (start with docs/01-getting-started.md)
├── tools/
│   ├── validate_pack.py   checks JSON, references, textures, lang keys
│   └── build_mcpack.py    validates, then zips pack/ into dist/*.mcpack
└── dist/          ← built .mcpack output (created by the build script)
```

## Quick start

```bash
python3 tools/validate_pack.py pack          # must print "0 error(s)"
python3 tools/build_mcpack.py                # writes dist/Smithing-Preview.mcpack
```

Then open the `.mcpack` on your device to import it, and enable it on a world.

## Guides

| # | Guide | What it covers |
|---|-------|----------------|
| 01 | [Getting started](docs/01-getting-started.md) | Install, build, test in game, where to start editing |
| 02 | [Pack layout](docs/02-pack-layout.md) | Folder structure and the old → new file map |
| 03 | [JSON UI concepts](docs/03-json-ui-concepts.md) | Namespaces, `@` inheritance, `$variables`, modifications, bindings |
| 04 | [Smithing screen](docs/04-smithing-screen.md) | Smithing table panels, the armor arc, the namespace rename |
| 05 | [Chests and containers](docs/05-chests-and-containers.md) | Chest layouts, overlays, collections, vanilla screen hooks |
| 06 | [Toggles, item data and common](docs/06-toggles-item-data-common.md) | Toggle manager, item movement buttons, shared controls |
| 07 | [Brewing guide](docs/07-brewing-guide.md) | Brewing stand panels, recipe book, factories and bindings |
| 08 | [Variables and item IDs](docs/08-variables-and-item-ids.md) | `_global_variables.json`, item ID tables, brewing mappings |
| 09 | [Textures, fonts and assets](docs/09-textures-fonts-assets.md) | Texture path rules, the `assets/` folder, the glyph font |
| 10 | [Localization](docs/10-localization.md) | Lang files, key parity, adding a language |
| 11 | [Validation and building](docs/11-validation-and-building.md) | What the validator checks and how to read its output |
| 12 | [Troubleshooting](docs/12-troubleshooting.md) | Common problems and fixes |
| 13 | [Known issues and roadmap](docs/13-known-issues-and-roadmap.md) | Open problems, what was not changed, next steps |

## Status

- The restructuring, namespace renames, and JSON formatting were checked with the validator
  (0 errors). The validator can't run the game, so **in-game behavior still needs to be
  tested** after each change.
- The changes in this rework are meant to leave the UI's behavior the same. See
  [13 — Known issues](docs/13-known-issues-and-roadmap.md) for what was deliberately left alone.
