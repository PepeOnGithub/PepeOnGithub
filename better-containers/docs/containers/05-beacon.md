# 05 — Beacon

Choosing beacon effects and the payment item.

## At a glance

| Field | Value |
|---|---|
| Vanilla screen | Beacon |
| File | `ui/beacon_screen.json` (vanilla override, keep the name) |
| Hook path | `beacon_panel/root_panel/beacon_inventory` |
| Operation | `insert_front` into `controls` |
| Inserted control | `bc_management_toggles.primary_management_toggles` |
| Variable | `$toggle_position: "right"` |

## What the pack adds

A row of management toggles on the right side of the screen: **reset**, **move**, and **drop**, with a status label.
These controls come from `ui/better_containers/shared/management_toggles.json`. Every screen that uses them gets the
same row, so a change to that file applies everywhere (see [10 — Shared controls](../10-shared-controls.md)).

## How the hook works

```json
"beacon_panel/root_panel/beacon_inventory": {
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
```

The game finds `beacon_panel/root_panel/beacon_inventory` in the vanilla screen and puts the row first in its `controls`, so it draws on top of the
vanilla layout. The pack doesn't change any other control on this screen.

## Notes for this container

The hook targets `beacon_inventory`, the inventory part of the beacon screen (by its name). The effect buttons are not touched.

## Change this container

- **Remove the row here only:** delete the `modifications` entry from `beacon_screen.json`. The row then doesn't appear on this screen, and nothing else changes.
- **Change the row everywhere:** edit `management_toggles.json`.
- **Move the row:** `right` is the only position the pack uses. Other values change a layout branch in `management_toggles.json` that is not used or tested here.
- **Add a container-specific control:** add a new `insert_front` or `insert_back` entry, and use `@` to instantiate a template from `bc_*` namespaces.

## Testing checklist

- [ ] The vanilla screen opens with no missing controls
- [ ] The reset, move, and drop toggles appear on the right
- [ ] The toggles work: each one selects its mode
- [ ] The vanilla slots and buttons still work
- [ ] The text fits at the smallest GUI scale and at the largest

## Troubleshooting

- **The row is missing:** the path in `beacon_screen.json` no longer matches the game's vanilla tree. Compare the path with the current vanilla UI (see [19 — Hooking a vanilla screen](../19-how-to-hook-a-vanilla-screen.md)).
- **The row overlaps a vanilla control:** check the order in the hook (`insert_front` puts it on top, `insert_back` puts it below).
- **The screen is blank:** run `python3 tools/validate_pack.py pack`, then check the JSON for a missing comma.

## Status

Built: an information panel, `ui/better_containers/containers/beacon_info.json`, hooked on the same path as the management row. It explains what the container does, in plain text from `data/container_info.json`. The management row is unchanged. The panel's position and whether its wrapped lines fit are not checked in game.

Before this panel, only the management row was added here. There's no container-specific layout yet. That's the next step if this screen needs more than the row (see [21 — Known issues](../21-known-issues-and-roadmap.md)).
