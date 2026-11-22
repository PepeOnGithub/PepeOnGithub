# 06 — Template catalog

A **template** is a control that other controls reuse with `@`. This guide tells you what exists, where it lives,
and which variables it declares, so you can reuse before you write something new.

- The **index** below is generated from the pack files. It lists every top-level control with the variables it
  declares (`$name|default`). Regenerate it after big changes (see the note at the end).
- "Declares" lists the variables with a default. Other `$variables` may be read without a default. Check the file.
- "Instances" are controls that inherit from another control with `@`. Nested controls aren't listed.

## Main templates and what they're for

| Template | Where | Purpose |
|---|---|---|
| `button` | `bc_shared` | Standard button built on `mappings` |
| `toggle`, `radio` | `bc_shared` | Toggle, and a toggle that belongs to a group |
| `item_movement_factory` | `bc_item_movement` | The five move/drop buttons for one item |
| `primary_management_toggles` | `bc_management_toggles` | Reset / move / drop row with its status label |
| `tab_left_button` | `bc_navigation` | One tab in a left-hand tab list |
| `tabbed_text_screen` | `bc_navigation` | Screen with a title bar and tabbed text |
| `container_elements` | `bc_chest_single` | All slot rows of a chest |
| `item_picker_icon` | `bc_smithing_table` | 16×16 item icon used as button content |
| `arc_primary_slot`, `arc_secondary_slot` | `bc_armor_arc` | One position on the armor arc |
| `potion_factory`, `*_ingredient_factory` | `bc_brewing_potion_slot` | One potion's result or ingredient slot |
| `recipe_book` | `bc_brewing_recipe_book` | The recipe book panel |
| `recipe_grid` | `bc_brewing_recipe_book` | The recipe grid |

## Index (generated)

| Namespace | Control | File | Declares |
|---|---|---|---|
| `bc_brewing_common` | `item_renderer` | `brewing/brewing_common.json` | — |
| `bc_brewing_common` | `item_slot_variables` | `brewing/brewing_common.json` | — |
| `bc_brewing_common` | `container_item_slot_overlay` | `brewing/brewing_common.json` | — |
| `bc_brewing_common` | `factory` | `brewing/brewing_common.json` | `$awkward_potion_action`, `$base_id`, `$brewing_factory_variables`, `$factory_binding_refrence`, `$factory_binding_values`, `$factory_control_identifiers`, `$factory_name`, `$fire_resistance_action`, `$harming_action`, `$healing_action`, `$infestation_action`, `$invisibility_action`, `$leaping_action`, `$night_vision_action`, `$oozing_action`, `$poison_action`, `$potion_prefix`, `$regeneration_action`, `$remainder`, `$slow_falling_action`, `$slowness_action`, `$strength_action`, `$swiftness_action`, `$turtle_master_action`, `$water_breathing_action`, `$weakness_action`, `$weaving_action`, `$wind_charging_action` |
| `bc_brewing_common` | `text_keys` | `brewing/brewing_common.json` | — |
| `bc_brewing_common` | `hover_text_renderer` | `brewing/brewing_common.json` | `$tooltip_anchor`, `$tooltip_offset` |
| `bc_brewing_common` | `empty_panel` | `brewing/brewing_common.json` | — |
| `bc_brewing_common` | `empty_label` | `brewing/brewing_common.json` | — |
| `bc_brewing_common` | `empty_image` | `brewing/brewing_common.json` | — |
| `bc_brewing_common` | `empty_stack` | `brewing/brewing_common.json` | — |
| `bc_brewing_common` | `empty_grid` | `brewing/brewing_common.json` | — |
| `bc_brewing_common` | `empty_collection` | `brewing/brewing_common.json` | — |
| `bc_brewing_common` | `custom_renderer` | `brewing/brewing_common.json` | — |
| `bc_brewing_common` | `root_panel` | `brewing/brewing_common.json` | — |
| `bc_brewing_factories` | `bindings` | `brewing/brewing_factories.json` | `$factory_bindings_index` |
| `bc_brewing_factories` | `potion_bindings` | `brewing/brewing_factories.json` | — |
| `bc_brewing_factories` | `splash_potion_bindings` | `brewing/brewing_factories.json` | — |
| `bc_brewing_factories` | `lingering_potion_bindings` | `brewing/brewing_factories.json` | — |
| `bc_brewing_factories` | `duration_potion_bindings` | `brewing/brewing_factories.json` | — |
| `bc_brewing_factories` | `potency_potion_bindings` | `brewing/brewing_factories.json` | — |
| `bc_brewing_factories` | `duration_splash_potion_bindings` | `brewing/brewing_factories.json` | — |
| `bc_brewing_factories` | `potency_splash_potion_bindings` | `brewing/brewing_factories.json` | — |
| `bc_brewing_factories` | `duration_lingering_potion_bindings` | `brewing/brewing_factories.json` | — |
| `bc_brewing_factories` | `potency_lingering_potion_bindings` | `brewing/brewing_factories.json` | — |
| `bc_brewing_toggles` | `secondary_toggle_properties` | `brewing/brewing_toggles.json` | — |
| `bc_brewing_toggles` | `secondary_toggle` | `brewing/brewing_toggles.json` | `$secondary_toggle_binding_value`, `$secondary_toggle_bindings`, `$secondary_toggle_control_name`, `$secondary_toggle_default_checked_index`, `$secondary_toggle_extra_properties`, `$secondary_toggle_forced_index`, `$secondary_toggle_mapping_type`, `$secondary_toggle_starts_active`, `$toggle_click_sound_volume`, `$toggle_collection_name` |
| `bc_brewing_toggles` | `toggle_properties` | `brewing/brewing_toggles.json` | — |
| `bc_brewing_toggles` | `toggle` | `brewing/brewing_toggles.json` | `$toggle_binding_value`, `$toggle_bindings`, `$toggle_click_sound_volume`, `$toggle_collection_name`, `$toggle_control_name`, `$toggle_default_checked_index`, `$toggle_extra_properties`, `$toggle_forced_index`, `$toggle_mapping_type`, `$toggle_starts_active` |
| `bc_brewing_toggles` | `tab_toggle` | `brewing/brewing_toggles.json` | — |
| `bc_brewing_toggles` | `bedrock_tab_toggle_properties` | `brewing/brewing_toggles.json` | `$extra_contents`, `$tab_checked_hover_texture`, `$tab_checked_texture`, `$tab_unchecked_hover_texture`, `$tab_unchecked_texture` |
| `bc_brewing_toggles` | `java_tab_toggle_properties` | `brewing/brewing_toggles.json` | `$extra_contents` |
| `bc_brewing_toggles` | `layout_toggle` | `brewing/brewing_toggles.json` | — |
| `bc_brewing_toggles` | `recipe_layout_toggle` | `brewing/brewing_toggles.json` | `$default_layout_texture`, `$hover_layout_texture`, `$recipe_book_close_control_name`, `$recipe_book_open_control_name` |
| `bc_brewing_toggles` | `layout_toggle_properties` | `brewing/brewing_toggles.json` | — |
| `bc_brewing_recipe_book` | `recolourful_recipe_book` | `brewing/recipe_book/recipe_book.json` | — |
| `bc_brewing_recipe_book` | `recipe_book` | `brewing/recipe_book/recipe_book.json` | `$base_id`, `$bedrock_checked_default_image`, `$bedrock_checked_default_image_left`, `$bedrock_checked_hover_image`, `$bedrock_checked_hover_image_left`, `$bedrock_unchecked_default_image`, `$bedrock_unchecked_default_image_left`, `$bedrock_unchecked_hover_image`, `$bedrock_unchecked_hover_image_left`, `$brewing_filter_texture`, `$brewing_grid_anchor_from`, `$brewing_grid_anchor_to`, `$brewing_grid_dimensions`, `$brewing_grid_filler_control`, `$brewing_grid_offset`, `$brewing_grid_position_0`, `$brewing_grid_position_1`, `$brewing_grid_position_10`, `$brewing_grid_position_11`, `$brewing_grid_position_12`, `$brewing_grid_position_13`, `$brewing_grid_position_14`, `$brewing_grid_position_15`, `$brewing_grid_position_16`, `$brewing_grid_position_17`, `$brewing_grid_position_18`, `$brewing_grid_position_19`, `$brewing_grid_position_2`, `$brewing_grid_position_3`, `$brewing_grid_position_4`, `$brewing_grid_position_5`, `$brewing_grid_position_6`, `$brewing_grid_position_7`, `$brewing_grid_position_8`, `$brewing_grid_position_9`, `$brewing_grid_size`, `$brewing_overlay_texture`, `$brewing_recipe_book_texture`, `$brewing_secondary_slot_texture`, `$brewing_slot_checkmark_texture`, `$brewing_slot_texture`, `$brewing_text_field_texture`, `$checkmark_texture_nineslice_size`, `$grid_item_renderer_anchor_point`, `$grid_item_renderer_offset`, `$grid_item_size`, `$index_offset`, `$java_checked_default_image`, `$java_unchecked_default_image`, `$recipe_overlay_nineslice_size`, `$recipe_overlay_offset`, `$recipe_overlay_size`, `$slot_hover_controller`, `$tab_toggle_type`, `$visible_condition` |
| `bc_brewing_recipe_book` | `recipe_grid` | `brewing/recipe_book/recipe_book.json` | — |
| `bc_brewing_recipe_book` | `grid_filler_panel` | `brewing/recipe_book/recipe_book.json` | — |
| `bc_brewing_recipe_book` | `highlight_slot_panel` | `brewing/recipe_book/recipe_book.json` | — |
| `bc_brewing_recipe_book` | `tab_template` | `brewing/recipe_book/recipe_book.json` | — |
| `bc_brewing_recipe_book` | `center_item_icon` | `brewing/recipe_book/recipe_book.json` | `$remainder` |
| `bc_brewing_recipe_book` | `recolourful_layout_toggle` | `brewing/recipe_book/recipe_book.json` | — |
| `bc_brewing_recipe_book` | `layout_toggle` | `brewing/recipe_book/recipe_book.json` | — |
| `bc_brewing_recipe_grid` | `recipe_book_grid` | `brewing/recipe_book/recipe_grid.json` | `$grid_item`, `$has_duration`, `$has_potency`, `$potion_prefix` |
| `bc_brewing_recipe_grid` | `item_toggle` | `brewing/recipe_book/recipe_grid.json` | `$item_index_id` |
| `bc_brewing_recipe_grid` | `recipe_grid_item` | `brewing/recipe_book/recipe_grid.json` | — |
| `bc_brewing_recipe_grid` | `primary_toggle_properties` | `brewing/recipe_book/recipe_grid.json` | `$duration_toggle_index` |
| `bc_brewing_recipe_grid` | `secondary_toggles` | `brewing/recipe_book/recipe_grid.json` | `$potency_toggle_index` |
| `bc_brewing_recipe_grid` | `potency_toggle` | `brewing/recipe_book/recipe_grid.json` | `$potion_prefix` |
| `bc_brewing_recipe_grid` | `secondary_toggle_properties` | `brewing/recipe_book/recipe_grid.json` | — |
| `bc_brewing_recipe_grid` | `craftable_slot` | `brewing/recipe_book/recipe_grid.json` | `$checkmark_bindings` |
| `bc_brewing_modifier_slot` | `duration_potion_factory` | `brewing/slots/modifier_slot.json` | — |
| `bc_brewing_modifier_slot` | `duration_ingredient_potion_factory` | `brewing/slots/modifier_slot.json` | — |
| `bc_brewing_modifier_slot` | `potency_potion_factory` | `brewing/slots/modifier_slot.json` | — |
| `bc_brewing_modifier_slot` | `potency_ingredient_potion_factory` | `brewing/slots/modifier_slot.json` | — |
| `bc_brewing_modifier_slot` | `duration_splash_potion_factory` | `brewing/slots/modifier_slot.json` | — |
| `bc_brewing_modifier_slot` | `duration_ingredient_splash_potion_factory` | `brewing/slots/modifier_slot.json` | — |
| `bc_brewing_modifier_slot` | `potency_splash_potion_factory` | `brewing/slots/modifier_slot.json` | — |
| `bc_brewing_modifier_slot` | `potency_ingredient_splash_potion_factory` | `brewing/slots/modifier_slot.json` | — |
| `bc_brewing_modifier_slot` | `duration_lingering_potion_factory` | `brewing/slots/modifier_slot.json` | — |
| `bc_brewing_modifier_slot` | `duration_ingredient_lingering_potion_factory` | `brewing/slots/modifier_slot.json` | — |
| `bc_brewing_modifier_slot` | `potency_lingering_potion_factory` | `brewing/slots/modifier_slot.json` | — |
| `bc_brewing_modifier_slot` | `potency_ingredient_lingering_potion_factory` | `brewing/slots/modifier_slot.json` | — |
| `bc_brewing_modifier_slot` | `glowstone_ingredient` | `brewing/slots/modifier_slot.json` | — |
| `bc_brewing_modifier_slot` | `redstone_ingredient` | `brewing/slots/modifier_slot.json` | — |
| `bc_brewing_potion_slot` | `slot_factory_template` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `brewing_result_item_slot` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `brewing_ingredient_item_slot` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `fuel_input_slot` | `brewing/slots/potion_slot.json` | `$remainder` |
| `bc_brewing_potion_slot` | `potion_ingredient_factory` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `splash_potion_ingredient_factory` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `lingering_potion_ingredient_factory` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `potion_factory` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `splash_potion_factory` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `lingering_potion_factory` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `water_bottle` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `awkward_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `night_vision_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `invisibility_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `leaping_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `fire_resistance_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `swiftness_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `slowness_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `water_breathing_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `healing_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `harming_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `poison_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `regeneration_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `strength_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `weakness_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `turtle_master_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `slow_falling_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `wind_charging_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `weaving_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `oozing_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `infestation_potion` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `awkward_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `night_vision_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `invisibility_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `leaping_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `fire_resistance_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `swiftness_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `slowness_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `water_breathing_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `healing_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `harming_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `poison_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `regeneration_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `strength_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `weakness_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `turtle_master_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `slow_falling_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `wind_charging_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `weaving_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `oozing_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `infestation_ingredients` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `dragons_breath_ingredient` | `brewing/slots/potion_slot.json` | — |
| `bc_brewing_potion_slot` | `gunpowder_ingredient` | `brewing/slots/potion_slot.json` | — |
| `(none)` | `container_item_bridge` | `compat/container_item_bridge.json` | `$base_id`, `$potion_prefix` |
| `(none)` | `container_item` | `compat/legacy_container_item.json` | — |
| `(none)` | `item_renderer` | `compat/legacy_container_item.json` | — |
| `bc_chest_double` | `container_elements` | `containers/chest_double.json` | — |
| `bc_chest_double` | `9x6_overlays` | `containers/chest_double.json` | `$item_collection_name` |
| `bc_chest_double` | `row_move_two_overlay` | `containers/chest_double.json` | — |
| `bc_chest_double` | `row_move_one_overlay` | `containers/chest_double.json` | — |
| `bc_chest_double` | `row_move_all_overlay` | `containers/chest_double.json` | — |
| `bc_chest_double` | `row_drop_all_overlay` | `containers/chest_double.json` | `$collection_index`, `$output_action`, `$row_index_offset` |
| `bc_chest_single` | `container_elements` | `containers/chest_single.json` | `$container_overlay_offset`, `$container_slot_highlight_control`, `$container_slot_pressed_control`, `$hotbar_overlay_offset`, `$hotbar_slot_highlight_control`, `$hotbar_slot_pressed_control`, `$inventory_overlay_offset`, `$inventory_slot_highlight_control`, `$inventory_slot_pressed_control`, `$row_index_offset`, `$search_field_default_control`, `$search_field_hover_control` |
| `bc_chest_single` | `9x1_overlays` | `containers/chest_single.json` | `$item_collection_name` |
| `bc_chest_single` | `9x3_overlays` | `containers/chest_single.json` | `$item_collection_name` |
| `bc_chest_single` | `row_move_two_overlay` | `containers/chest_single.json` | — |
| `bc_chest_single` | `row_move_one_overlay` | `containers/chest_single.json` | — |
| `bc_chest_single` | `row_move_all_overlay` | `containers/chest_single.json` | — |
| `bc_chest_single` | `row_drop_all_overlay` | `containers/chest_single.json` | `$collection_index`, `$output_action`, `$row_index_offset` |
| `bc_chest_single` | `hotbar_row_move_two_overlay` | `containers/chest_single.json` | — |
| `bc_chest_single` | `hotbar_row_move_one_overlay` | `containers/chest_single.json` | — |
| `bc_chest_single` | `hotbar_row_move_all_overlay` | `containers/chest_single.json` | — |
| `bc_chest_single` | `hotbar_row_drop_all_overlay` | `containers/chest_single.json` | `$collection_index`, `$output_action`, `$row_index_offset` |
| `bc_chest_single` | `grid_row` | `containers/chest_single.json` | — |
| `bc_chest_single` | `default_cell_control` | `containers/chest_single.json` | — |
| `bc_chest_single` | `row_highlight_control` | `containers/chest_single.json` | — |
| `bc_item_movement` | `item_movement_factory` | `shared/item_movement.json` | `$hover_control` |
| `bc_item_movement` | `input_area_template` | `shared/item_movement.json` | `$movement_action_control` |
| `bc_item_movement` | `move_one` | `shared/item_movement.json` | — |
| `bc_item_movement` | `move_two` | `shared/item_movement.json` | — |
| `bc_item_movement` | `move_all` | `shared/item_movement.json` | — |
| `bc_item_movement` | `drop_one` | `shared/item_movement.json` | — |
| `bc_item_movement` | `drop_all` | `shared/item_movement.json` | — |
| `bc_management_toggles` | `primary_management_toggles` | `shared/management_toggles.json` | `$button_default_texture`, `$button_hover_texture`, `$button_pressed_texture`, `$button_texture_nineslice`, `$icon_reset_texture`, `$icon_texture_default_color`, `$icon_texture_drop`, `$icon_texture_hover_color`, `$icon_texture_move`, `$icon_texture_offset`, `$icon_texture_reset_size`, `$icon_texture_size`, `$ignore_status_bar`, `$management_toggle_size`, `$row_icon_offset`, `$row_icon_size`, `$row_icon_texture`, `$status_label_anchor`, `$status_label_anchor_offset`, `$status_label_property_text`, `$toggle_label_color`, `$toggle_label_underlay_offset`, `$toggle_label_underlay_texture`, `$toggle_label_underlay_texture_nineslice`, `$toggle_label_underlay_uv`, `$toggle_label_underlay_uv_size`, `$toggle_stack_controls` |
| `bc_management_toggles` | `right_row_toggles` | `shared/management_toggles.json` | — |
| `bc_management_toggles` | `button_holder_template` | `shared/management_toggles.json` | — |
| `bc_navigation` | `title_bar` | `shared/navigation.json` | — |
| `bc_navigation` | `tab_icon_frame` | `shared/navigation.json` | — |
| `bc_navigation` | `tab_left_button` | `shared/navigation.json` | — |
| `bc_navigation` | `navigation_tabs` | `shared/navigation.json` | `$navigation_tabs` |
| `bc_navigation` | `scroll_content` | `shared/navigation.json` | `$scroll_content` |
| `bc_navigation` | `title_label` | `shared/navigation.json` | — |
| `bc_navigation` | `tabbed_text_screen` | `shared/navigation.json` | `$tab_text_panel` |
| `bc_navigation` | `inventory_icon_image` | `shared/navigation.json` | — |
| `bc_navigation` | `recipe_book_icon_image` | `shared/navigation.json` | — |
| `bc_navigation` | `tab_toggle_light` | `shared/navigation.json` | — |
| `bc_navigation` | `tab_toolbar` | `shared/navigation.json` | — |
| `bc_shared` | `redstone_content` | `shared/shared_controls.json` | `$search_field_default_control`, `$search_field_hover_control` |
| `bc_shared` | `input_panel_with_index` | `shared/shared_controls.json` | — |
| `bc_shared` | `text_edit_control` | `shared/shared_controls.json` | — |
| `bc_shared` | `input_panel_overlay` | `shared/shared_controls.json` | — |
| `bc_shared` | `mappings` | `shared/shared_controls.json` | `$button_output_action`, `$consume_event` |
| `bc_shared` | `button` | `shared/shared_controls.json` | — |
| `bc_shared` | `toggle` | `shared/shared_controls.json` | `$radio_toggle_group`, `$toggle_default_state`, `$toggle_group_default_selected`, `$toggle_group_forced_index` |
| `bc_shared` | `radio` | `shared/shared_controls.json` | — |
| `bc_shared` | `button_visuals` | `shared/shared_controls.json` | `$icon_path`, `$toggle_is_hover` |
| `bc_shared` | `toggle_texture_template` | `shared/shared_controls.json` | `$icon_color` |
| `bc_armor_arc` | `arc_primary` | `smithing/armor_arc.json` | — |
| `bc_armor_arc` | `arc_primary_positions` | `smithing/armor_arc.json` | — |
| `bc_armor_arc` | `arc_primary_slot` | `smithing/armor_arc.json` | — |
| `bc_armor_arc` | `arc_primary_slot_base` | `smithing/armor_arc.json` | `$rotation_x`, `$rotation_y`, `$slider_value` |
| `bc_armor_arc` | `arc_slider` | `smithing/armor_arc.json` | — |
| `bc_armor_arc` | `arc_secondary` | `smithing/armor_arc.json` | — |
| `bc_armor_arc` | `arc_secondary_positions` | `smithing/armor_arc.json` | — |
| `bc_armor_arc` | `arc_secondary_slot` | `smithing/armor_arc.json` | — |
| `bc_armor_arc` | `arc_secondary_slot_base` | `smithing/armor_arc.json` | `$rotation_x`, `$rotation_y`, `$slider_value` |
| `bc_smithing_table` | `item_picker_icon` | `smithing/smithing_table.json` | `$item_id`, `$item_id_aux` |
| `bc_smithing_table` | `item_picker_toggle` | `smithing/smithing_table.json` | — |
| `bc_smithing_table` | `toggle_row` | `smithing/smithing_table.json` | — |
| `bc_smithing_table` | `item_picker_panel` | `smithing/smithing_table.json` | — |
| `bc_smithing_table` | `armor_tab_icon` | `smithing/smithing_table.json` | — |
| `bc_smithing_table` | `template_tab_icon` | `smithing/smithing_table.json` | — |
| `bc_smithing_table` | `mineral_tab_icon` | `smithing/smithing_table.json` | — |
| `bc_smithing_table` | `smithing_tabs` | `smithing/smithing_table.json` | — |
| `bc_smithing_table` | `tab_text_stack` | `smithing/smithing_table.json` | — |
| `bc_smithing_table` | `armor_arc_group` | `smithing/smithing_table.json` | — |
| `bc_smithing_table` | `armor_preview_button` | `smithing/smithing_table.json` | — |
| `bc_smithing_table` | `smithing_table_screen` | `smithing/smithing_table.json` | — |

## Regenerating this index

The index is produced by reading every JSON file under `pack/ui/better_containers/` and listing each top-level key
whose value is an object (except `namespace`, `$…`, and `#…`). Run `python3 tools/validate_pack.py pack` first to
confirm the references are still valid, then update this table.

## Adding a template

1. Name it with a role and a suffix (see [03 — Naming conventions](03-naming-conventions.md)).
2. Declare every screen-specific value as `$variable|default`.
3. Put it in the feature folder, or in `shared/` if two or more features use it.
4. Reference it with `@` from the instance, and set only the variables you need.
5. Add a row to the index and a line to the main table if it's broadly useful.
