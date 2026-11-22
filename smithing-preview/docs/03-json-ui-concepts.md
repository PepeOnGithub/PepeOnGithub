# 03 — JSON UI concepts

This pack relies on the standard Bedrock JSON UI system. Read this before the screen guides.

## Files and namespaces

Every custom file starts with a `namespace`. Each top-level key in that file is then a named
**control** that other files can use.

```json
{
  "namespace": "smithing",
  "l_0oe": { "type": "panel", "size": ["100% - 4px", "100% - 4px"], "controls": [] }
}
```

`l_0oe` is now `smithing.l_0oe`. Other files use it as `smithing.l_0oe`.

- A custom file must be listed in `ui/_ui_defs.json` to load. The 15 files listed there do.
  Vanilla override files at the `ui/` root are applied by their own names.
- Some files are **not** listed (see 13). Don't assume they load. Test them in game.

## Inheritance with `@`

A key with `@` creates an instance of another control. The part before `@` is the name in
the current file. The part after is the source.

```json
"o_8iy@smithing.lg_1e": { "controls": [ ... ] }
```

- Left of `@` = the new name (`o_8iy`).
- Right of `@` = the control to copy (`smithing.lg_1e`). Its properties are inherited,
  and the properties you write here override them.
- `@` on a key with an empty body (`{}`) just instantiates the control as-is.

Common targets are vanilla controls such as `common.root_panel`, `common.item_renderer`, and
`common.text_edit_box`. These come from vanilla and are not defined in this pack.

## `$variables`

Variables let one template behave differently per instance. The form `$name|default` sets a
default, which the instance can override.

```json
"$item_id|default": 0,          // default value in the template
"gho_66@common_toggles.light_content_toggle": {
  "$button_content": "smithing.l_0oe"   // override for this instance
}
```

Variables are used for item IDs, texture paths, control names, and output actions. Global
values live in `ui/_global_variables.json` (see 08).

## Modifications

A `modifications` array changes an existing control without copying it. Each entry has an
`operation`, usually on a `controls` or `bindings` array:

| Operation | Effect |
|---|---|
| `insert_front` / `insert_back` | add entries at the start or end |
| `insert_before` / `insert_after` | add next to a named control |
| `remove` | delete a named control or array entry |
| `replace` | replace a named control |

The examples in this pack target vanilla screens (for example `chest_panel`, `anvil_screen_inventory`)
using paths with `/` (`root_panel/chest_panel`).

## Bindings and `#properties`

A `bindings` array connects a value from one control (or a collection of items) to a property
on another control.

```json
{
  "binding_type": "view",
  "source_property_name": "(#full_item_id + #item_id)",
  "target_property_name": "#item_id_aux"
}
```

- `binding_type` is one of `view`, `collection`, `collection_details`, or `global`. The pack
  uses `view` most (about 180 times).
- `#name` is a **property**. It holds state that bindings and conditions read.
  Common ones here: `#visible`, `#toggle_state`, `#item_selected_index`, `#item_name`,
  `#slider_value`.
- The `__is_*_key` / `__potency_*` properties are set by the brewing factories (see 07).

## `property_bag` and `variables`

- `property_bag` sets initial values for `#properties` on a control.
- `variables` (a list with `requires` conditions) selects a control to use based on
  `$item_collection_name`. The brewing slots use this to pick ingredient, result, or fuel slots.

## Checking your work

`tools/validate_pack.py` checks that every `name@namespace.key` reference in the pack resolves
to a real key. It doesn't check bindings or property names, so those still need in-game testing.
