# 04 — Migration map

Every renamed file, namespace, control, texture, and variable, with its name in the original upload. Use this table to update your own notes, edits, or references to the old names. The tables were generated from the mapping that migrated the pack, so they match the files.

Four rounds of renames happened. Round 4 renamed the project and its prefix:

| Original (round 3) | Current (round 4) |
|---|---|
| Project name `Smithing Preview`, repo folder `smithing-preview/` | `Better Containers`, repo folder `better-containers/` |
| Namespace prefix `sp_` (for example `sp_smithing_table`) | `bc_` (for example `bc_smithing_table`) |
| Variable prefix `$sp_brewing:` | `$bc_brewing:` |
| UI folder `ui/smithing_preview/` | `ui/better_containers/` |
| Texture folder `textures/smithing_preview/` | `textures/better_containers/` |
| Build output `Smithing-Preview.mcpack` | `Better-Containers.mcpack` |

The manifest name, description, and UUIDs were regenerated for the new name.

Three rounds of renames happened: round 1 (folders and three generated namespaces), round 2 (the smithing and navigation controls, the file names, and the texture tree), and round 3 (every nested control and binding ID). All three are listed here.

## Files

| Original upload path | Current path |
|---|---|
| `ui/pepe/_global.json` | `ui/better_containers/shared/shared_controls.json` |
| `ui/pepe/item_data.json` | `ui/better_containers/shared/item_movement.json` |
| `ui/pepe/toggle_manager.json` | `ui/better_containers/shared/management_toggles.json` |
| `ui/pepe/uic.json` | `ui/better_containers/shared/navigation.json` |
| `ui/pepe/single_chest_content.json` | `ui/better_containers/containers/chest_single.json` |
| `ui/pepe/double_chest_content.json` | `ui/better_containers/containers/chest_double.json` |
| `ui/pepe/smithing.json` | `ui/better_containers/smithing/smithing_table.json` |
| `ui/pepe/smithing_arc.json` | `ui/better_containers/smithing/armor_arc.json` |
| `ui/pepe/brewing_guide/brewing_global.json` | `ui/better_containers/brewing/brewing_common.json` |
| `ui/pepe/brewing_guide/factory_bindings.json` | `ui/better_containers/brewing/brewing_factories.json` |
| `ui/pepe/brewing_guide/brewing_toggle.json` | `ui/better_containers/brewing/brewing_toggles.json` |
| `ui/pepe/brewing_guide/inventory_area/brewing_potion_slot.json` | `ui/better_containers/brewing/slots/potion_slot.json` |
| `ui/pepe/brewing_guide/inventory_area/modifier_brewing_potion_slot.json` | `ui/better_containers/brewing/slots/modifier_slot.json` |
| `ui/pepe/brewing_guide/recipe_book_area/brewing_recipe_book.json` | `ui/better_containers/brewing/recipe_book/recipe_book.json` |
| `ui/pepe/brewing_guide/recipe_book_area/brewing_recipe_book_grid.json` | `ui/better_containers/brewing/recipe_book/recipe_grid.json` |
| `ui/pepe/common/compatibility/advanced/compatibility_container_item.json` | `ui/better_containers/compat/container_item_bridge.json` |
| `ui/ui_common.json` | `ui/better_containers/compat/legacy_container_item.json` |
| `ui/pepe/brewing_guide/**` | `ui/better_containers/brewing/**` (folder changed, see the file rows above) |
| `ui/_global_variables.json`, `ui/_ui_defs.json`, vanilla `ui/*_screen.json` | unchanged location |

## Namespaces

| Original upload namespace | Current namespace |
|---|---|
| `bd-h1` | `bc_smithing_table` |
| `f-ez18` | `bc_armor_arc` |
| `es1e-` | `bc_navigation` |
| `_global` | `bc_shared` |
| `item_data` | `bc_item_movement` |
| `uic` | `bc_navigation` |
| `toggle_manager` | `bc_management_toggles` |
| `single_chest_content` | `bc_chest_single` |
| `double_chest_content` | `bc_chest_double` |
| `smithing` | `bc_smithing_table` |
| `smithing_arc` | `bc_armor_arc` |
| `brewing_global` | `bc_brewing_common` |
| `factory_bindings` | `bc_brewing_factories` |
| `brewing_toggle` | `bc_brewing_toggles` |
| `brewing_potion_slot` | `bc_brewing_potion_slot` |
| `modifier_brewing_potion_slot` | `bc_brewing_modifier_slot` |
| `brewing_recipe_book` | `bc_brewing_recipe_book` |
| `brewing_recipe_book_grid` | `bc_brewing_recipe_grid` |

## Controls (generated IDs)

| Original ID | Current name | Defined in |
|---|---|---|
| `mx_7x` | `title_bar` | `better_containers/shared/navigation.json` |
| `nw_3p` | `tab_icon_frame` | `better_containers/shared/navigation.json` |
| `lg_0t` | `tab_left_button` | `better_containers/shared/navigation.json` |
| `zxh7_6` | `navigation_tabs` | `better_containers/shared/navigation.json` |
| `d-3fa` | `scroll_content` | `better_containers/shared/navigation.json` |
| `ms_y87` | `title_label` | `better_containers/shared/navigation.json` |
| `yw8d5_` | `tabbed_text_screen` | `better_containers/shared/navigation.json` |
| `w_t4f` | `inventory_icon_image` | `better_containers/shared/navigation.json` |
| `dnj-72` | `recipe_book_icon_image` | `better_containers/shared/navigation.json` |
| `fs_3m` | `tab_toggle_light` | `better_containers/shared/navigation.json` |
| `c0z-m` | `tab_toolbar` | `better_containers/shared/navigation.json` |
| `l_0oe` | `item_picker_icon` | `better_containers/smithing/smithing_table.json` |
| `gho_66` | `item_picker_toggle` | `better_containers/smithing/smithing_table.json` |
| `lg_1e` | `toggle_row` | `better_containers/smithing/smithing_table.json` |
| `dl_s72` | `item_picker_panel` | `better_containers/smithing/smithing_table.json` |
| `tw9-g` | `armor_tab_icon` | `better_containers/smithing/smithing_table.json` |
| `ew5i6_` | `template_tab_icon` | `better_containers/smithing/smithing_table.json` |
| `qj0s-` | `mineral_tab_icon` | `better_containers/smithing/smithing_table.json` |
| `a-ux76` | `armor_preview_button` | `better_containers/smithing/smithing_table.json` |
| `m_0kh` | `smithing_tabs` | `better_containers/smithing/smithing_table.json` |
| `uy9o_9` | `tab_text_stack` | `better_containers/smithing/smithing_table.json` |
| `gf7_9o` | `armor_arc_group` | `better_containers/smithing/smithing_table.json` |
| `r_fi52` | `smithing_table_screen` | `better_containers/smithing/smithing_table.json` |
| `j2-wh` | `arc_primary` | `better_containers/smithing/armor_arc.json` |
| `e3_d7x` | `arc_primary_positions` | `better_containers/smithing/armor_arc.json` |
| `p_9a6u` | `arc_primary_slot` | `better_containers/smithing/armor_arc.json` |
| `ae_m5` | `arc_primary_slot_base` | `better_containers/smithing/armor_arc.json` |
| `zk24-s` | `arc_slider` | `better_containers/smithing/armor_arc.json` |
| `g8_sj` | `arc_secondary` | `better_containers/smithing/armor_arc.json` |
| `wof-69` | `arc_secondary_positions` | `better_containers/smithing/armor_arc.json` |
| `aq_i6` | `arc_secondary_slot` | `better_containers/smithing/armor_arc.json` |
| `i_2ro` | `arc_secondary_slot_base` | `better_containers/smithing/armor_arc.json` |

## Textures and assets

| Original | Current |
|---|---|
| `textures/button_assets/*.png` | `textures/better_containers/buttons/*.png` |
| `textures/copper`, `drop`, `move`, `reset`, `row_icon` (.png) | `textures/better_containers/icons/*.png` (names unchanged) |
| `textures/label_underlay`, `status_label_underlay` (.png) | `textures/better_containers/backgrounds/*.png` |
| `textures/ui/ashur/cell_icons/*`, `textures/ui/ashur/white_slot` | `textures/better_containers/slots/*.png` |
| `assets/brewing_guide/recipe_book.png` | `textures/better_containers/brewing/recipe_book/background.png` |
| `assets/brewing_guide/sprites/recipe_book/*` | `textures/better_containers/brewing/recipe_book/sprites/*` |
| `textures/ui/pepe/**` (intermediate round-1 path) | removed; see rows above |
| `font/glyph_E0.png` | unchanged (the game requires `font/`) |

## Variables

| Original | Current |
|---|---|
| `$brewing_guide:<item>` | `$bc_brewing:<item>` |

## Every control rename (round 2 and 3)

Each row is one control, with the file where it is defined. Nested controls get a numeric suffix when a file already has a control with the same role.

| File | Original | Current |
|---|---|---|
| `shared/item_movement.json` | `move_2_overlay` | `input_panel_overlay` |
| `shared/management_toggles.json` | `item_management_stack_1` | `stack_panel` |
| `shared/navigation.json` | `mx_7x` | `title_bar` |
| `shared/navigation.json` | `g4pr0_` | `image` |
| `shared/navigation.json` | `nw_3p` | `tab_icon_frame` |
| `shared/navigation.json` | `hv_0r9` | `_tab_icon` |
| `shared/navigation.json` | `lg_0t` | `tab_left_button` |
| `shared/navigation.json` | `zxh7_6` | `navigation_tabs` |
| `shared/navigation.json` | `znp-3` | `_navigation_tabs` |
| `shared/navigation.json` | `d-3fa` | `scroll_content` |
| `shared/navigation.json` | `yd8-0j` | `_scroll_content` |
| `shared/navigation.json` | `ms_y87` | `title_label` |
| `shared/navigation.json` | `yw8d5_` | `tabbed_text_screen` |
| `shared/navigation.json` | `p_xn9` | `navigation_tabs_2` |
| `shared/navigation.json` | `v0a-2s` | `common_panel` |
| `shared/navigation.json` | `q_n3y` | `stack_panel` |
| `shared/navigation.json` | `u-f0i` | `panel` |
| `shared/navigation.json` | `fj0_8x` | `_tab_text_panel` |
| `shared/navigation.json` | `y6aw7_` | `container_scroll_panel` |
| `shared/navigation.json` | `w_t4f` | `inventory_icon_image` |
| `shared/navigation.json` | `dnj-72` | `recipe_book_icon_image` |
| `shared/navigation.json` | `fs_3m` | `tab_toggle_light` |
| `shared/navigation.json` | `kd57j_` | `light_content_toggle` |
| `shared/navigation.json` | `c0z-m` | `tab_toolbar` |
| `shared/navigation.json` | `l-r3p8` | `toolbar_background` |
| `shared/navigation.json` | `x7yj8-` | `stack_panel_2` |
| `shared/navigation.json` | `p_wn9` | `panel_2` |
| `shared/navigation.json` | `v8m_g` | `tab_toggle_light_2` |
| `shared/navigation.json` | `vp6_9h` | `panel_3` |
| `shared/navigation.json` | `bg_i4` | `tab_toggle_light_3` |
| `shared/navigation.json` | `c_65qi` | `panel_4` |
| `shared/navigation.json` | `r7xg_` | `panel_5` |
| `shared/navigation.json` | `y0bq_9` | `light_close_button` |
| `shared/navigation.json` | `df0-t` | `panel_6` |
| `smithing/smithing_table.json` | `l_0oe` | `item_picker_icon` |
| `smithing/smithing_table.json` | `ep_0j` | `item_renderer` |
| `smithing/smithing_table.json` | `gho_66` | `item_picker_toggle` |
| `smithing/smithing_table.json` | `lg_1e` | `toggle_row` |
| `smithing/smithing_table.json` | `dl_s72` | `item_picker_panel` |
| `smithing/smithing_table.json` | `x4-1wv` | `stack_panel` |
| `smithing/smithing_table.json` | `o_8iy` | `toggle_row_2` |
| `smithing/smithing_table.json` | `l7z_h` | `item_picker_toggle_2` |
| `smithing/smithing_table.json` | `n3_j8y` | `item_picker_toggle_3` |
| `smithing/smithing_table.json` | `g4uk-9` | `item_picker_toggle_4` |
| `smithing/smithing_table.json` | `i-yx6` | `item_picker_toggle_5` |
| `smithing/smithing_table.json` | `sh_53o` | `item_picker_toggle_6` |
| `smithing/smithing_table.json` | `z_xt9` | `item_picker_toggle_7` |
| `smithing/smithing_table.json` | `bz-g3` | `toggle_row_3` |
| `smithing/smithing_table.json` | `j7t_u9` | `item_picker_toggle_8` |
| `smithing/smithing_table.json` | `x2q7-e` | `item_picker_toggle_9` |
| `smithing/smithing_table.json` | `m-u8w6` | `item_picker_toggle_10` |
| `smithing/smithing_table.json` | `g0g_4d` | `item_picker_toggle_11` |
| `smithing/smithing_table.json` | `d3-zf` | `item_picker_toggle_12` |
| `smithing/smithing_table.json` | `l5p-7n` | `item_picker_toggle_13` |
| `smithing/smithing_table.json` | `y3f_9f` | `toggle_row_4` |
| `smithing/smithing_table.json` | `x64c_f` | `item_picker_toggle_14` |
| `smithing/smithing_table.json` | `f0k-n4` | `item_picker_toggle_15` |
| `smithing/smithing_table.json` | `o8q-g` | `item_picker_toggle_16` |
| `smithing/smithing_table.json` | `z_zg2` | `item_picker_toggle_17` |
| `smithing/smithing_table.json` | `lu-5i` | `item_picker_toggle_18` |
| `smithing/smithing_table.json` | `n-7y7w` | `item_picker_toggle_19` |
| `smithing/smithing_table.json` | `x8p-8m` | `toggle_row_5` |
| `smithing/smithing_table.json` | `us8_v` | `item_picker_toggle_20` |
| `smithing/smithing_table.json` | `urh9-` | `item_picker_toggle_21` |
| `smithing/smithing_table.json` | `h9-4xp` | `item_picker_toggle_22` |
| `smithing/smithing_table.json` | `g5c_q` | `item_picker_toggle_23` |
| `smithing/smithing_table.json` | `em-79n` | `item_picker_toggle_24` |
| `smithing/smithing_table.json` | `ln95k_` | `item_picker_toggle_25` |
| `smithing/smithing_table.json` | `x_n3u` | `toggle_row_6` |
| `smithing/smithing_table.json` | `gu40p-` | `item_picker_toggle_26` |
| `smithing/smithing_table.json` | `xp_8b1` | `stack_panel_2` |
| `smithing/smithing_table.json` | `gr20t-` | `toggle_row_7` |
| `smithing/smithing_table.json` | `m-ug5` | `item_picker_toggle_27` |
| `smithing/smithing_table.json` | `rc_t7` | `item_picker_toggle_28` |
| `smithing/smithing_table.json` | `wf1_d9` | `item_picker_toggle_29` |
| `smithing/smithing_table.json` | `g_y6m3` | `item_picker_toggle_30` |
| `smithing/smithing_table.json` | `grt-4` | `item_picker_toggle_31` |
| `smithing/smithing_table.json` | `of_51k` | `item_picker_toggle_32` |
| `smithing/smithing_table.json` | `z1k_8z` | `toggle_row_8` |
| `smithing/smithing_table.json` | `xi3s-` | `item_picker_toggle_33` |
| `smithing/smithing_table.json` | `ch8j_` | `item_picker_toggle_34` |
| `smithing/smithing_table.json` | `cv2w_1` | `item_picker_toggle_35` |
| `smithing/smithing_table.json` | `c5kh-` | `item_picker_toggle_36` |
| `smithing/smithing_table.json` | `a4te_0` | `item_picker_toggle_37` |
| `smithing/smithing_table.json` | `tm4e_6` | `item_picker_toggle_38` |
| `smithing/smithing_table.json` | `w5sd-` | `toggle_row_9` |
| `smithing/smithing_table.json` | `jj43g_` | `item_picker_toggle_39` |
| `smithing/smithing_table.json` | `u-2wi` | `item_picker_toggle_40` |
| `smithing/smithing_table.json` | `bq_4n` | `item_picker_toggle_41` |
| `smithing/smithing_table.json` | `o3_fd` | `item_picker_toggle_42` |
| `smithing/smithing_table.json` | `qg-2e` | `item_picker_toggle_43` |
| `smithing/smithing_table.json` | `g4o9-p` | `toggle_row_10` |
| `smithing/smithing_table.json` | `m-b8y` | `item_picker_toggle_44` |
| `smithing/smithing_table.json` | `ro61m_` | `toggle_row_11` |
| `smithing/smithing_table.json` | `p6u4g-` | `item_picker_toggle_45` |
| `smithing/smithing_table.json` | `msa-6` | `item_picker_toggle_46` |
| `smithing/smithing_table.json` | `h-t30s` | `item_picker_toggle_47` |
| `smithing/smithing_table.json` | `v-zn3` | `item_picker_toggle_48` |
| `smithing/smithing_table.json` | `k_yp8` | `item_picker_toggle_49` |
| `smithing/smithing_table.json` | `tyt0-` | `item_picker_toggle_50` |
| `smithing/smithing_table.json` | `xv-m9` | `toggle_row_12` |
| `smithing/smithing_table.json` | `p5b1n-` | `item_picker_toggle_51` |
| `smithing/smithing_table.json` | `jm02-g` | `item_picker_toggle_52` |
| `smithing/smithing_table.json` | `c6-dv` | `item_picker_toggle_53` |
| `smithing/smithing_table.json` | `xi5u-` | `item_picker_toggle_54` |
| `smithing/smithing_table.json` | `u7_ox7` | `item_picker_toggle_55` |
| `smithing/smithing_table.json` | `tw9-g` | `armor_tab_icon` |
| `smithing/smithing_table.json` | `ew5i6_` | `template_tab_icon` |
| `smithing/smithing_table.json` | `qj0s-` | `mineral_tab_icon` |
| `smithing/smithing_table.json` | `m_0kh` | `smithing_tabs` |
| `smithing/smithing_table.json` | `v8y7e_` | `tab_left_button` |
| `smithing/smithing_table.json` | `e8y2_w` | `tab_left_button_2` |
| `smithing/smithing_table.json` | `uy9o_9` | `tab_text_stack` |
| `smithing/smithing_table.json` | `c4b6d-` | `panel` |
| `smithing/smithing_table.json` | `z5-0zo` | `title_label` |
| `smithing/smithing_table.json` | `hgg-4` | `title_label_2` |
| `smithing/smithing_table.json` | `mg_2x` | `title_label_3` |
| `smithing/smithing_table.json` | `gf7_9o` | `armor_arc_group` |
| `smithing/smithing_table.json` | `h-5sf` | `arc_secondary` |
| `smithing/smithing_table.json` | `iz7_s` | `arc_primary` |
| `smithing/smithing_table.json` | `z-i75l` | `arc_slider` |
| `smithing/smithing_table.json` | `a-ux76` | `armor_preview_button` |
| `smithing/smithing_table.json` | `r_fi52` | `smithing_table_screen` |
| `smithing/smithing_table.json` | `h9_ke` | `tabbed_text_screen` |
| `smithing/smithing_table.json` | `qa7g_` | `title_bar` |
| `smithing/smithing_table.json` | `p_z7n` | `root_panel` |
| `smithing/smithing_table.json` | `v_c9z` | `tab_toolbar` |
| `smithing/smithing_table.json` | `e_dl9` | `common_panel` |
| `smithing/smithing_table.json` | `evf-61` | `light_content_toggle` |
| `smithing/smithing_table.json` | `l9-u5e` | `panel_2` |
| `smithing/smithing_table.json` | `vs66_y` | `armor_arc_group_2` |
| `smithing/smithing_table.json` | `c-7wz` | `panel_3` |
| `smithing/smithing_table.json` | `r-e7m` | `top_half_panel` |
| `smithing/smithing_table.json` | `oy-o65` | `inventory_panel_bottom_half_with_label` |
| `smithing/smithing_table.json` | `j_f9p` | `hotbar_grid_template` |
| `smithing/smithing_table.json` | `v4or_` | `inventory_take_progress_icon_button` |
| `smithing/smithing_table.json` | `pdn6-` | `inventory_selected_icon_button` |
| `smithing/smithing_table.json` | `e2-ks` | `gamepad_cursor_button` |
| `smithing/smithing_table.json` | `k_9qf6` | `panel_4` |
| `smithing/armor_arc.json` | `j2-wh` | `arc_primary` |
| `smithing/armor_arc.json` | `rw5-z` | `arc_primary_positions_2` |
| `smithing/armor_arc.json` | `e3_d7x` | `arc_primary_positions` |
| `smithing/armor_arc.json` | `nw5o5_` | `arc_primary_slot_2` |
| `smithing/armor_arc.json` | `xy-w1` | `arc_primary_slot_3` |
| `smithing/armor_arc.json` | `oq9h_` | `arc_primary_slot_4` |
| `smithing/armor_arc.json` | `b_ww93` | `arc_primary_slot_5` |
| `smithing/armor_arc.json` | `f_d8n` | `arc_primary_slot_6` |
| `smithing/armor_arc.json` | `p_9a6u` | `arc_primary_slot` |
| `smithing/armor_arc.json` | `fx24_k` | `arc_primary_slot_base_2` |
| `smithing/armor_arc.json` | `tm-e4` | `arc_primary_slot_base_3` |
| `smithing/armor_arc.json` | `ai7v2_` | `arc_primary_slot_base_4` |
| `smithing/armor_arc.json` | `v8_ur` | `arc_primary_slot_base_5` |
| `smithing/armor_arc.json` | `d_4tj6` | `arc_primary_slot_base_6` |
| `smithing/armor_arc.json` | `x0hf-` | `arc_primary_slot_base_7` |
| `smithing/armor_arc.json` | `u9g9-v` | `arc_primary_slot_base_8` |
| `smithing/armor_arc.json` | `a7-xj` | `arc_primary_slot_base_9` |
| `smithing/armor_arc.json` | `xm72-t` | `arc_primary_slot_base_10` |
| `smithing/armor_arc.json` | `u_d1m` | `arc_primary_slot_base_11` |
| `smithing/armor_arc.json` | `o8pv_` | `arc_primary_slot_base_12` |
| `smithing/armor_arc.json` | `gd35_c` | `arc_primary_slot_base_13` |
| `smithing/armor_arc.json` | `ad1t_` | `arc_primary_slot_base_14` |
| `smithing/armor_arc.json` | `ae_m5` | `arc_primary_slot_base` |
| `smithing/armor_arc.json` | `b7wi-3` | `custom` |
| `smithing/armor_arc.json` | `zk24-s` | `arc_slider` |
| `smithing/armor_arc.json` | `a5zm6_` | `panel` |
| `smithing/armor_arc.json` | `y_h25x` | `slider` |
| `smithing/armor_arc.json` | `pa_c7` | `empty_panel` |
| `smithing/armor_arc.json` | `u77f-p` | `panel_2` |
| `smithing/armor_arc.json` | `n_j7k` | `slider_2` |
| `smithing/armor_arc.json` | `g8_sj` | `arc_secondary` |
| `smithing/armor_arc.json` | `wof-69` | `arc_secondary_positions` |
| `smithing/armor_arc.json` | `e4v-w9` | `arc_secondary_slot_2` |
| `smithing/armor_arc.json` | `p-dd4` | `arc_secondary_slot_3` |
| `smithing/armor_arc.json` | `ch9n_` | `arc_secondary_slot_4` |
| `smithing/armor_arc.json` | `gaj1-9` | `arc_secondary_slot_5` |
| `smithing/armor_arc.json` | `aq_i6` | `arc_secondary_slot` |
| `smithing/armor_arc.json` | `c-4cf1` | `arc_secondary_slot_base_2` |
| `smithing/armor_arc.json` | `n64mc_` | `arc_secondary_slot_base_3` |
| `smithing/armor_arc.json` | `x5x-j` | `arc_secondary_slot_base_4` |
| `smithing/armor_arc.json` | `t-u90c` | `arc_secondary_slot_base_5` |
| `smithing/armor_arc.json` | `xv7r_` | `arc_secondary_slot_base_6` |
| `smithing/armor_arc.json` | `ev_m5` | `arc_secondary_slot_base_7` |
| `smithing/armor_arc.json` | `d0ph4_` | `arc_secondary_slot_base_8` |
| `smithing/armor_arc.json` | `d-53zn` | `arc_secondary_slot_base_9` |
| `smithing/armor_arc.json` | `o_4hz2` | `arc_secondary_slot_base_10` |
| `smithing/armor_arc.json` | `p6_al` | `arc_secondary_slot_base_11` |
| `smithing/armor_arc.json` | `ziv89_` | `arc_secondary_slot_base_12` |
| `smithing/armor_arc.json` | `fl_53l` | `arc_secondary_slot_base_13` |
| `smithing/armor_arc.json` | `t45x-d` | `arc_secondary_slot_base_14` |
| `smithing/armor_arc.json` | `i_2ro` | `arc_secondary_slot_base` |
| `smithing/armor_arc.json` | `y88pg_` | `custom_2` |

## Binding identifiers

These are toggle and tab binding IDs, which were generated strings. They are referenced by value across files.

| Original | Current |
|---|---|
| `go1-s` | `tab_binding_01` |
| `a9nc_` | `tab_binding_02` |
| `u_c5x` | `tab_binding_03` |
| `w-c8l` | `toggle_binding_01` |
| `al_7q` | `toggle_binding_02` |
| `j-8bp` | `toggle_binding_03` |
| `n9-dm` | `toggle_binding_04` |
| `aa57f_` | `toggle_binding_05` |
| `pb8_r8` | `toggle_binding_06` |
| `mc35-p` | `toggle_binding_07` |
| `s9f_s` | `toggle_binding_08` |
| `r-3i4j` | `toggle_binding_09` |
| `nw4-p` | `toggle_binding_10` |
| `kz6v_` | `toggle_binding_11` |
| `e0uv_` | `toggle_binding_12` |
| `t-u7v` | `toggle_binding_13` |
| `r4u8s_` | `toggle_binding_14` |
| `c1s-4m` | `toggle_binding_15` |
| `qt2_r1` | `toggle_binding_16` |
| `z7x_m` | `toggle_binding_17` |
| `pn_0j` | `toggle_binding_18` |
| `f8_ze` | `toggle_binding_19` |
| `l4-aw` | `toggle_binding_20` |
| `gg_p9` | `toggle_binding_21` |
| `m_zu81` | `toggle_binding_22` |
| `y_9zp6` | `toggle_binding_23` |
| `h6p-e5` | `toggle_binding_24` |
| `h-xb58` | `toggle_binding_25` |
| `zf8-p` | `toggle_binding_26` |
| `vah8_` | `toggle_binding_27` |
| `i5i_l` | `toggle_binding_28` |
| `z69n-y` | `toggle_binding_29` |
| `m2c_x9` | `toggle_binding_30` |
| `u-j80e` | `toggle_binding_31` |
| `mu_7w` | `toggle_binding_32` |
| `mv-a2` | `toggle_binding_33` |
| `g_3vn3` | `toggle_binding_34` |
| `aa7_f7` | `toggle_binding_35` |
| `d_0kt0` | `toggle_binding_36` |
| `w_7en` | `toggle_binding_37` |
| `kr9_p9` | `toggle_binding_38` |
| `jr_4o1` | `toggle_binding_39` |
| `id55-v` | `toggle_binding_40` |
| `vd-2m1` | `toggle_binding_41` |
| `z8xw-` | `toggle_binding_42` |
| `p-o4k` | `toggle_binding_43` |
| `uyv-2` | `toggle_binding_44` |
| `wr1e_` | `toggle_binding_45` |
| `m9k_q` | `toggle_binding_46` |
| `hjl0_` | `toggle_binding_47` |
| `vk9y6_` | `toggle_binding_48` |
| `y4a-l7` | `toggle_binding_49` |
| `dlb4_` | `toggle_binding_50` |
| `k5rf_` | `toggle_binding_51` |
| `rhm3_2` | `toggle_binding_52` |
| `eng3_` | `toggle_binding_53` |
| `g_aa02` | `toggle_binding_54` |
| `y-8sp5` | `toggle_group_01` |
| `vh9_z8` | `toggle_group_02` |
| `qpf7_5` | `toggle_group_03` |
| `jy_8w4` | `toggle_group_04` |
