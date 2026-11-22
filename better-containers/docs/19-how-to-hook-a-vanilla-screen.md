# 19 — How to hook a vanilla screen

Use this guide to add a pack control to a vanilla screen, such as a toggle row on the anvil.

## How hooks work

A vanilla override file lives at the root of `ui/` and keeps its vanilla name, for example `anvil_screen.json`.
It uses `modifications` to add or remove controls in the vanilla tree.

```json
{
  "anvil_panel/root_panel/anvil_screen_inventory": {
    "modifications": [
      {
        "array_name": "controls",
        "operation": "insert_front",
        "value": {
          "primary_elements@bc_management_toggles.primary_management_toggles": { "$toggle_position": "right" }
        }
      }
    ]
  }
}
```

- The key is the **path** to the vanilla control: `anvil_panel/root_panel/anvil_screen_inventory`.
- `operation` says what to do. `insert_front` puts the new control first in `controls`.
- `value` is the pack control to add, using `@` to instantiate a template.

## Steps

1. **Find the vanilla path.** Use the vanilla UI for the game version you target. Note the names from the root down to the control.
2. **Create the file at the `ui/` root** if it doesn't exist, and name it after the vanilla screen (`<screen>_screen.json`).
3. **Add the hook** with a `modifications` entry, as above. Use the same key style as the existing hooks.
4. **Check the existing hooks** in `chest_screen.json`, `anvil_screen.json`, `beacon_screen.json`, and `smithing_table_2_screen.json` for examples.
5. **Validate.** Run the validator. It checks the pack side of the reference.
6. **Test in game** on the screen you hooked. A wrong path usually shows as a missing control, not a crash.

## Where hooks live today

| Screen | File | Adds |
|---|---|---|
| Smithing table | `smithing_table_2_screen.json` | `smithing_table_screen` and the management toggles |
| Chests | `chest_screen.json` | `container_elements` for each chest |
| Anvil | `anvil_screen.json` | Management toggles |
| Beacon | `beacon_screen.json` | Management toggles |

## When a hook breaks

- After a game update, vanilla names can change. Start with the path in the hook.
- If the screen opens but the control is missing, check the path, then the `operation`.
- Keep vanilla override files at the `ui/` root. Their names must match the game's, so don't move them into `better_containers/`.
