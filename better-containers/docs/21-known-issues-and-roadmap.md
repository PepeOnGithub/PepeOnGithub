# 21 — Known issues and roadmap

This guide lists what the revamp changed, what it deliberately left alone, and what still needs work.

## What this revamp did

- Moved every UI file into a feature folder under `ui/better_containers/` (see [02](02-folder-structure.md)).
- Renamed every pack namespace with the `bc_` prefix, and every generated control name to a role name.
- Renamed every nested generated name (about 160) to a role name, with a numeric suffix when a file has more than one instance.
- Renamed binding identifiers (about 60) to readable names such as `toggle_binding_01`.
- Put every pack texture under `textures/better_containers/`, grouped by type.
- Renamed the variable prefix from `$brewing_guide:` to `$bc_brewing:`.
- Added `manifest.json` (the upload had none), and moved the archive contents to the root.
- Added the validator and build script, and wrote the guides in `docs/`.
- Renamed the project to **Better Containers**: prefix `sp_` → `bc_`, folders and build output renamed to match.
- Added one guide per vanilla container in `docs/containers/` (14 guides).

Every rename was applied to every reference in one pass, and the validator confirmed that every namespace and `%key` reference still resolves.
The local references (`source_control_name`, `control_name`) match the original upload exactly: the same 76 are unresolved before and after.

## What it deliberately did not change

- **Logic.** Every control and binding keeps its behavior. The pack is about 160 KB of interdependent JSON, and without a way to run
  Minecraft, a logic rewrite would likely break it. The changes here are structural. Gameplay and visuals are intended to be the same,
  but that **still needs to be confirmed in game**.
- **Template merges.** The two armor arcs are parallel sets, not one template. Merging them changes bindings and defaults (see [08](08-armor-arc.md)).
  The three smithing tab icons are also similar, but each has its own fixed item. This is the next template candidate.
- **Vanilla override files.** Their names must match the game, so they stay at the `ui/` root.

## Open issues

### 1. Duplicate key in `legacy_container_item.json`

`container_item` appears twice at the top level. JSON parsers keep one value, and the game may keep either. The file came from `ui/ui_common.json` and was
moved to `compat/` without changes. It is not in `_ui_defs.json`, so it may be unused. The validator reports it as a known warning.

- If it is not used in game, delete it.
- If it is used, decide which definition is meant to win, then merge the two into one key.

### 2. `container_item_bridge.json` isn't in `_ui_defs.json`

The file exists but isn't listed. It was not listed in the original upload either, so its behavior is unchanged.
Test in game with and without it listed, then add it if it's meant to load.

### 3. References to controls the pack doesn't define

76 control references point to names that aren't defined in the pack. Some are vanilla controls, such as `brewing_guide_toggle`
and `flying_item_renderer`. Others are built at runtime (for example `'potion_item_' + $factory_bindings_index + '01'`).

Some are probably missing, and the original upload had them too. These include `potion_tab`, `potion_slot_factory`,
`potion_ingredient_slot_factory`, and `lingering_potion_slot_factory`. In game, check whether these names resolve. If not, define them or update the references.

### 4. Numbered suffixes

Nested controls in the same file that share a role get a numeric suffix (for example `arc_primary_slot_2`). That's correct,
but a suffix doesn't tell you what makes each instance different. Give each instance a clearer name when you next edit it.

### 5. Vanilla textures and paths

24 vanilla texture paths and the vanilla screen hooks depend on the game version. Re-check them after each Minecraft update.

### 6. Numeric item IDs

The IDs in `_global_variables.json` weren't verified against game data (see [14](14-variables-and-item-ids.md)).

### 7. Missing metadata

- No `pack_icon.png`, so the pack has no icon when imported.
- No `min_engine_version` in the manifest. Set it to the lowest version you tested.
- The manifest UUIDs were made from fixed names, so they're stable across builds. Give the pack its own UUIDs if you publish it next to another pack.

## Still not built

The items below are what still needs work, and why.

- **Brewing filter:** built by `tools/build_brewing_filter.py`. Each recipe-grid potion is a fixed control, so its polarity comes from `data/potion_polarity.json` and is written as `$polarity_control`. Four radio toggles (All, Good, Bad, Mixed) at the bottom of the recipe book show or hide grid items. Each filter shows its own packed grid. Unverified in game: the row position, the `(#filter_all or #filter_match)` visibility binding, and the checked/unchecked textures (`craft_toggle_on`/`off`).

- Information panels for the seven management-row containers are built. Positions and text wrapping must be checked in game.

## Roadmap

0. **Container-specific layouts.** Eleven containers only get the management row. Decide, one container at a time, whether it needs its own layout, and start from the guide in `docs/containers/`.

1. **Test in game.** Check the smithing table, the armor arc, chests and double chests, the brewing stand, and the recipe book.
2. **Decide on open issues 1 and 3.** Those decide whether the brewing and compat files are used at all.
3. **Templatize the smithing tab icons.** They differ only by their item variable. Merge them into one template with a parameter, then test.
4. **Decide the armor arc merge.** Compare the two arcs' bindings in game before merging.
5. **Add `pack_icon.png` and `min_engine_version`.**

## Audit against the vanilla UI (data/wiki/audit.md)

Fixed: every guide and info panel is now a vertical stack that anchors to the right of the hooked panel instead of covering the inventory; `toolbar_background` inherits the real vanilla template; an unused third-party layout toggle was removed from the brewing recipe book; the smithing guide and management toggles now sit inside the custom smithing screen (the old hook path sat under a removed panel and never applied).

Panel fit: guides are now 108 px wide (6 cells) with two tabs per row, so a guide beside the 176 px screen needs a GUI width of about 400, which is GUI scale 4 on a 1080p display. At scale 5 or higher on 1080p the guide is cut off by the screen edge; JSON UI cannot read the GUI scale, so there is no automatic fallback.

Mode toggles: JSON UI cannot write a global binding, so the `'#mode_' + $toggle_view_binding_name` binding (copied from the original pack, never written by anything) stays inert and is left as it was. The real mode state is now wired through view bindings: each mode button has two labels bound to its own `#toggle_state`, and the active one shows in green while the others stay white. The status label above the buttons already reads the same states. Unverified in game: the label colour swap.

Brewing filter gaps: fixed. Each filter (Good, Bad, Mixed) has its own grid with only the matching potions packed from the first cell, so hiding leaves no holes. The All grid is unchanged. `tools/build_brewing_filter.py` builds the grids from `data/potion_polarity.json`.

Open: phone (`*_pocket`) layouts get no guide.
