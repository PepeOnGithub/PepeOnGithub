# 17 — Validation and building

## `tools/validate_pack.py`

```bash
python3 tools/validate_pack.py pack
```

It uses only the standard library. Exit code `0` means no errors; `1` means at least one error. Warnings never fail the run.

### What it checks

| Check | Result when it fails |
|---|---|
| Every `.json` file parses (comments are allowed) | ERROR |
| Every file listed in `ui/_ui_defs.json` exists, and none is listed twice | ERROR |
| Every `textures/` and `assets/` path inside the pack resolves to a PNG | ERROR |
| Vanilla texture paths (`textures/ui/...`) that the pack doesn't ship | WARN, summarized |
| Every language file has exactly the keys of `en_US.lang`, with no duplicates | ERROR |
| Every `%key` used in UI JSON exists in `en_US.lang` | ERROR |
| No duplicate keys inside one object (a parser would silently drop one) | ERROR, except known files (WARN) |
| No reference to a retired namespace name (for example `single_chest_content`) | ERROR |
| Every `name@namespace.key` reference into a pack namespace resolves | WARN, summarized |
| Custom files in `ui/better_containers/` that aren't in `_ui_defs.json` | WARN |
| Control references (`source_control_name`, `control_name`) that match no key in the pack | WARN, with a count |

### Reading the output

```
Checked 34 JSON files, 42 texture refs, 15 pack namespaces.
WARN  not listed in _ui_defs: ui/better_containers/compat/container_item_bridge.json
WARN  24 vanilla texture path(s) not shipped in the pack ...
WARN  76 control reference(s) match no pack control (vanilla or built at runtime), e.g. brewing_guide_toggle
0 error(s), 5 warning(s)
```

- **ERROR**: something is definitely broken. Fix it before you test.
- **WARN**: something is intentional, or can't be checked offline. Read it, then decide.
- The 76 control references are the same ones that were in the original upload. They point to vanilla controls or names built at runtime.

### What it doesn't check

- Whether a numeric item ID is the right item.
- Whether property names and bindings do what you intend.
- How anything looks. Test in game.

## `tools/sync_item_ids.py`

Checks every `$<item>_item_id` against the item list in `data/item_ids/stable-1.26.60.json` (the list the Minecraft Item ID
Viewer uses). It reports each mismatch. Add `--write` to correct them. Brewing potion-type values are not checked.

```bash
python3 tools/sync_item_ids.py           # report
python3 tools/sync_item_ids.py --write   # correct
```

## `tools/build_guides.py`

Generates all five in-game guide panels (furnace, enchanting, anvil, smithing, chest) and hooks them into their vanilla screens. Re-run after you change a guide. See [the guides index](guides/README.md).

## `tools/build_mcpack.py`

```bash
python3 tools/build_mcpack.py                      # writes dist/Better-Containers.mcpack
python3 tools/build_mcpack.py out/custom.mcpack    # custom output path
```

The build runs the validator first and stops on any error. The archive has its files at the root, with `manifest.json` at the top level.

## Extending the validator

Each numbered section in `main()` is one check. Add a new check in the same style: collect errors into `ERRORS` and warnings into
`WARNINGS`. The summary prints both at the end.
