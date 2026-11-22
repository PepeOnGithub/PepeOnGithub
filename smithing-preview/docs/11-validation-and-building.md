# 11 — Validation and building

## `tools/validate_pack.py`

```bash
python3 tools/validate_pack.py pack
```

No third-party packages. It exits with `0` when there are no errors, and `1` when there is at least one.
Warnings don't fail the run.

### What it checks

| # | Check | Result |
|---|-------|--------|
| 1 | Every `.json` parses (comments allowed) | Error |
| 2 | Every file in `_ui_defs.json` exists | Error |
| 3 | Custom `_ui_defs` entries are not listed twice | Error |
| 4 | Every `textures/` and `assets/` path resolves to a file | Error for pack paths |
| 5 | Vanilla textures (`textures/ui/...`, not under `pepe/` or `ashur/`) | Warning, summarized |
| 6 | Every language file has the same keys as `en_US` and no duplicate keys | Error |
| 7 | Every `%key` used in UI JSON exists in `en_US.lang` | Error |
| 8 | Every `name@namespace.key` reference into a pack namespace resolves | Warning, summarized |
| 9 | Custom files in `ui/pepe/` that are not listed in `_ui_defs` | Warning |

### Reading the output

```
Checked 34 JSON files, 42 texture refs, 15 pack namespaces.
WARN  not listed in _ui_defs: ui/pepe/compat/compatibility_container_item.json
WARN  24 vanilla texture path(s) not shipped in the pack, assumed present in vanilla (e.g. textures/ui/TabTopBack)
0 error(s), 2 warning(s)
```

- **ERROR** — something is definitely broken. Fix it before testing.
- **WARN** — something is intentional or can't be checked offline. Read it, then decide.
- Check 8 can warn about references to vanilla namespaces with the same name as a pack namespace
  (for example `_global`). Those are likely fine.

### What it doesn't check

- Whether a numeric item ID matches the real item.
- Whether `#properties` and bindings do what you intend.
- How anything looks. Test in game.

## `tools/build_mcpack.py`

```bash
python3 tools/build_mcpack.py                    # dist/Smithing-Preview.mcpack
python3 tools/build_mcpack.py out/custom.mcpack  # custom output path
```

It runs the validator first and refuses to build on any error. The archive holds the files at its root,
with `manifest.json` at the top level.

## Adding checks

The validator is a single file. Each numbered section in `main()` is one check. Add a new check in the
same style: collect errors into `ERRORS` and warnings into `WARNINGS`, then the summary prints them.
