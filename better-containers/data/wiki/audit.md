# Pack audit against vanilla UI (bedrock-samples)

Method: all 201 vanilla `resource_pack/ui` files listed in the sample repo's `_ui_defs.json` were downloaded and parsed.
The pack (51 JSON files at audit time; `stonecutter_*` was added during the audit) was checked by script against them.
Note: `common.json`, `common_buttons.json` and `common_toggles.json` do NOT exist as files in bedrock-samples (404).
The `common`, `common_buttons`, `common_toggles`, `common_tabs` namespaces live in `ui_common.json`, `ui_template_*.json` etc., so lookups were done by namespace, not file name.

## 1. The "88 unresolved control references" warning

`tools/validate_pack.py` only prints the first one. All 88 are `source_control_name` / `control_name` values.
Breakdown (checked by script, with line numbers from the pack):

- 87 are NOT bugs: the control is created at runtime from a variable used as a control NAME in a template (`"$var@template"`).
  - `$toggle_view_binding_name` -> `shared/shared_controls.json:164` (`bc_shared.toggle`) and vanilla `common_toggles.light_ui_toggle` (ui_template_toggles.json:590-599). Covers `*_tab_toggle`, `move_*_row`, `drop_all_row`, `toggle_mode_reset`, `eng_2`, `ilm_4`, `jtv_1`, `ojk_43`, `toggle_binding_01..54`.
  - `$tab_view_binding_name` -> vanilla `common_tabs.tab` (ui_template_tabs.json:94). Covers `tab_binding_01..03`.
  - `$factory_name` -> `brewing/brewing_common.json:231`. Covers `*potion*_slot_factory`, `*_ingredient_slot_factory`.
  - `$toggle_control_name` / `$recipe_book_open_control_name` -> `brewing/brewing_toggles.json:105,306`. Covers `potion_tab`, `splash_potion_tab`, `lingering_potion_tab`, `brewing_guide_toggle`.
  - `$text_edit_text_control` -> vanilla `ui_common.json:1734/1847` (`utility_search_box`).
  - Every one of the 87 names is assigned somewhere in the pack and every referenced `toggle_binding_NN` / `tab_binding_NN` is assigned (script-verified).
- 1 is a vanilla control: `flying_item_renderer` (`pack/ui/brewing_stand_screen.json:12`, `insert_before`). It is a direct child of `brewing_stand_panel` in vanilla, OK.
- Harmless leftovers: `toggle_binding_02` (`shared/navigation.json:240`) and `toggle_binding_26` are assigned but never read.

Conclusion: the warning has no real missing control. Suggestion for the validator: also treat any string value assigned to a `$...` variable as a defined name, so the warning goes to 0.

Real unresolved references found by the broader `@ns.key` scan (the validator MISSES these because it only checks pack namespaces):

| # | file:line | reference | status |
|---|---|---|---|
| A | `pack/ui/better_containers/shared/navigation.json:189` | `toolbar_background@crafting.toolbar_background` | `crafting` namespace (inventory_screen.json) has no `toolbar_background`. Only `loom`, `trade2`, `smithing_table_2`, `stonecutter` define one (images of `textures/ui/toolbar_background`); inventory_screen.json:2232 itself uses `@common.toolbar_background_image`. REAL BUG: the toolbar background image is not drawn. |
| B | `pack/ui/better_containers/brewing/recipe_book/recipe_book.json:466` | `recolourful_layout_toggle@compatibility_common.general_recipe_toggle` | namespace `compatibility_common` does not exist in vanilla nor in the pack (third-party Recolourful pack). Control is not used anywhere. REAL BUG (definition error in the content log). |

Fixes:
- A: change key to `"toolbar_background@common.toolbar_background_image"` (keeps the `size`, `anchor_*`, `layer` overrides).
- B: delete the whole `recolourful_layout_toggle` block (`recipe_book.json:466-474`), or rebase it on `@bc_brewing_toggles.recipe_layout_toggle`.

## 2. Inherited templates / hooks / bindings

- Every `@ns.key` and every string value of the form `ns.key` (e.g. `$tab_panel`, `$template_toggle`, `$button_content`) that points to a vanilla namespace was resolved against vanilla. Only A and B above fail. All `common.*`, `common_toggles.*`, `common_tabs.*`, `bc_*` references are fine (including `common_toggles.light_content_toggle`, `common_tabs.tab_left`, `common.text_edit_box`, `common.edit_box_indent(_hover)`, `common.inventory_panel_bottom_half_with_label`).
- All hook paths in `pack/ui/*_screen.json` (including the new stonecutter one) resolve through vanilla inheritance chains: `small_chest_panel/root_panel/chest_panel`, `large_chest_panel/...`, `right_panel/furnace_screen_inventory`, `anvil_panel/root_panel/anvil_screen_inventory`, `horse_panel/root_panel`, `player_inventory`, `panel/root_panel/redstone_screen_inventory`, `brewing_stand_panel` + `flying_item_renderer`, `brewing_panel_top_half`, `smithing_table_panel` etc. `blast_furnace_screen` and `smoker_screen` keys exist in vanilla (blast furnace is `@furnace.furnace_screen`, so `$is_blast_furnace` propagates).
- Bindings present in vanilla: `#hover_text`, `#item_id_aux`, `#furnace_flame_ratio`, `#furnace_arrow_ratio`, `#brewing_fuel_ratio`, `#clip_ratio`, `#collection_length`, `#item_custom_color`, `#armor_trim_material/pattern`, `#slider_value/#slider_steps`, `#close_button_visible`, `#disabled_filter_visible`, `#filtered_light_multiplier`, `#item_name`, `#text_box_item_name`, `#property_field`, `#toggle_state`, `#visible`, `#offset`. All the rest (`#item_index_*`, `#p1..p18`, `#status_index_*`, `#is_*`, `#*_trim_item`, `#*_item_id`, `#mode_*`, ...) are pack-defined via `property_bag` / `binding_name_override` / `target_property_name`.
- `#toggle_state` view bindings by control name all point at real toggle-typed controls (runtime-named, see section 1).
- Unverifiable from vanilla: `shared/shared_controls.json:185` uses a `binding_type: global` binding named `('#mode_' + $toggle_view_binding_name)` and `#toggle_mode_reset`, `#move_one` etc. These names are not engine globals in vanilla; they only work if the game exposes a toggle's state as a global by its name. Test in game; if the mode toggles do nothing, this is the first place to look.
- Low risk: `pack/ui/smithing_table_2_screen.json:5-8` `remove` of `root_panel` has no `"array_name": "controls"`. Fix: add `"array_name": "controls"` (brewing_stand_screen.json already does).
- Medium risk: the same file's second hook (`smithing_table_panel/root_panel/smithing_table_screen_inventory`, adds `primary_elements` and `smithing_guide`) targets a subtree of the very `root_panel` that the first modification removes, and `bc_smithing_table.smithing_table_screen` contains neither `smithing_guide` nor `primary_management_toggles` (grep). Likely those two never appear. Fix: put `primary_elements@bc_management_toggles.primary_management_toggles` and `smithing_guide@bc_smithing_guide.smithing_guide` directly in `smithing_table_screen` (`smithing/smithing_table.json:726`) or in the `insert_back` value, and drop the deep-path hook.
- `compat/*.json` are not in `_ui_defs.json` and have no `namespace`, so they are inert (known, docs/21). Consequence: the search-box dimming (`#disabled_filter_visible`) is never applied.
- Only desktop panels are hooked (e.g. `chest.small_chest_panel`); the `*_pocket` variants (`pocket_containers.*`, `*_screen_pocket.json`) get no guide on phone UI profile.

## 3. Guide / info panels vs the vanilla panels (OVERLAP DEFECT, all 14)

Files: `pack/ui/better_containers/containers/{chest_guide,furnace_guide,anvil_guide,enchanting_guide,smithing_guide,beacon_info,cartography_info,grindstone_info,horse_info,inventory_info,loom_info,stonecutter_info,trade_info}.json` (chest_guide 60 wide, all others 144 wide).

Each root is `"type": "panel"`, `"size": [144 (60 for chest), "default"]`, `"layer": 2` with NO `anchor_from`, `anchor_to` or `offset`, and none of the hooks (`pack/ui/*_screen.json`) pass any. Consequences, by static analysis against vanilla geometry:
1. Default anchor is `center`. The vanilla hooked panels are `common.root_panel` = 176x166 (large chest 176x220, beacon 256x219, stonecutter 146x166 area). A 144-wide guide centered in a 176x166 panel covers the player inventory (162 wide, `inventory_panel_bottom_half_with_label` is 100% x 93, `hotbar_grid_template` 162x18) and the machine slots. The chest guide (60 wide) sits on the middle chest slots.
2. `"default"` height on a `panel` is not content height; it behaves like the parent's size. Use `"100%c"`.
3. The roots are plain `panel`s, so their children (title label, bars, text rows, tab bars, `info_lines`) are all stacked on top of each other in the same spot (e.g. `furnace_guide.json:36-`, `chest_guide.json:11-`, `grindstone_info.json:11-`). Only inner `info_lines` / `tab_bar` / `*_panel` are stack panels.

Suggested exact fix, same edit in all 13 files, replacing the root's header:
```json
"furnace_guide": {
  "type": "stack_panel",
  "orientation": "vertical",
  "size": [144, "100%c"],
  "anchor_from": "top_left",
  "anchor_to": "top_right",
  "offset": [24, 0],
  "layer": 2,
```
(for `chest_guide` use `[60, "100%c"]`; offset 24 leaves room for the 18px management toggles that `primary_management_toggles` puts on the right edge; use `anchor_from: "top_right"`, `anchor_to": "top_left"`, `offset: [-4, 0]` for screens where `$toggle_position` is `left`, e.g. chests.) Children of a stack_panel need explicit heights (title_label 12, bars 6, rows 10 are OK; `"default"` heights on `info_lines` and `tab_contents` should become `"100%c"`). Alternative if the side space is too small (a 144-wide guide only fits beside a 176 panel at GUI scale <=4 on 1080p): anchor `top_middle`/`bottom_middle` below the panel with `size [176, "100%c"]`.

## 4. Other defects

- `furnace_guide.json:864-902` `progress_bar`: the flame bar uses `$bar_clip: left`; vanilla flame uses `clip_direction: "down"` (furnace_screen.json:169-179). Cosmetic. Also the `track` has no background, so an empty bar is invisible.
- `shared/navigation.json:240` / `toggle_binding_02` and `toggle_binding_26` are assigned but unused (harmless).

## Most serious (5 lines)
1. All 13 guide/info panels have no anchor/offset and a plain `panel` root with `"default"` height: they render centered over the vanilla 176x166 inventory and their children pile on one another (fix in section 3).
2. `shared/navigation.json:189` `@crafting.toolbar_background` does not exist in vanilla (use `@common.toolbar_background_image`).
3. `brewing/recipe_book/recipe_book.json:466` references namespace `compatibility_common` (third-party, nonexistent): delete the block.
4. `smithing_table_2_screen.json` removes `root_panel` and then hooks inside it, so the smithing guide and management toggles are likely never inserted; also add `array_name` to the `remove`.
5. The 88-reference warning hides no real missing control (87 runtime-named via `$var@template`, 1 vanilla); the validator misses the two real ones above.
