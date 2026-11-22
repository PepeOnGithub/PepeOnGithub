# 05 — JSON UI concepts

The pack uses the standard Bedrock JSON UI system. Learn these five ideas and the rest of the guides make sense.

## 1. Namespaces

Each custom file starts with a `namespace`. Every top-level key in that file becomes a named control
that other files can use, written as `namespace.name`.

```json
{
  "namespace": "bc_smithing_table",
  "smithing_table_screen": { "type": "panel", "size": ["100%", "100%"], "controls": [] }
}
```

Another file uses it as `bc_smithing_table.smithing_table_screen`.

## 2. Templates and inheritance with `@`

A key with `@` creates an **instance** of a template. The part before `@` is the instance's name in the current
file. The part after `@` is the template to copy.

```json
"item_picker_toggle@common_toggles.light_content_toggle": {
  "$button_content": "bc_smithing_table.item_picker_icon",
  "size": [22, 22]
}
```

- Left of `@`: the instance name (`item_picker_toggle`).
- Right of `@`: the template (`common_toggles.light_content_toggle`, a vanilla control).
- Properties written in the instance override the template's properties.
- An empty body `{}` creates the instance exactly as the template defines it.

A template is any control that is meant to be reused. In this pack, templates are named with a suffix
(`_template`, `_factory`) or simply a role name (`toggle_row`). See [06 — Template catalog](06-template-catalog.md).

## 3. Variables (`$`)

Variables let one template behave differently per instance.

```json
"$item_id|default": 0,
"property_bag": { "#item_id": "($item_id * 65536)" }
```

- `$name|default` gives a default. An instance can set `"$name": value` to override it.
- Variables are inserted into the control when it's built. They're not runtime state.
- Global variables live in `ui/_global_variables.json` and are read by name, for example `$armor_items_tab_item_id`.

## 4. Properties (`#`) and bindings

`#name` is a **property**: runtime state that a control holds. Bindings connect properties between controls.

```json
"bindings": [
  {
    "binding_type": "view",
    "source_property_name": "(#full_item_id + #item_id)",
    "target_property_name": "#item_id_aux"
  }
]
```

| `binding_type` | Use |
|---|---|
| `view` | Connect a property of this control to a property of another (most common) |
| `collection` / `collection_details` | Read item or slot data from an item collection |
| `global` | Read a global game value |

Common properties in this pack: `#visible`, `#toggle_state`, `#item_selected_index`, `#item_name`, `#slider_value`.

## 5. Modifications

A `modifications` array changes an existing control without copying it. Use it to hook into vanilla.

| `operation` | Effect |
|---|---|
| `insert_front` / `insert_back` | Add entries at the start or end of an array such as `controls` |
| `insert_before` / `insert_after` | Add next to a named control |
| `remove` | Delete a named control |
| `replace` | Replace a named control |

## Templating rules this pack follows

- A template has a name, default variables (`|default`), and no screen-specific content.
- A screen instantiates a template with `@`, and only sets the variables it needs.
- Shared templates live in `shared/` and are referenced by every feature. Feature-specific templates stay in their feature folder.
- A template should be used in at least one place, or it should be removed.

## Validation

`tools/validate_pack.py` checks that every `namespace.name` reference resolves, that every `%lang` key exists, that
no key is duplicated, and that every texture path exists. It does not check property names or bindings, so test those in game.
