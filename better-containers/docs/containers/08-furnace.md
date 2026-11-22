# 08 — Furnace

Smelting and smoking food, and smelting ore.

## At a glance

| Field | Value |
|---|---|
| Vanilla screen | Furnace |
| File | `ui/furnace_screen.json` (vanilla override, keep the name) |
| Hook path | `right_panel/furnace_screen_inventory` |
| Operation | `insert_front` into `controls` |
| Inserted control | `bc_management_toggles.primary_management_toggles` |
| Variable | `$toggle_position: "right"` |

## What the pack adds

A row of management toggles on the right side of the screen: **reset**, **move**, and **drop**, with a status label.
These controls come from `ui/better_containers/shared/management_toggles.json`. Every screen that uses them gets the
same row, so a change to that file applies everywhere (see [10 — Shared controls](../10-shared-controls.md)).

## How the hook works

```json
"right_panel/furnace_screen_inventory": {
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

The game finds `right_panel/furnace_screen_inventory` in the vanilla screen and puts the row first in its `controls`, so it draws on top of the
vanilla layout. The pack doesn't change any other control on this screen.

## Notes for this container

The hook path starts at `right_panel`, not `root_panel`. The pack does not hook the blast furnace or the smoker. Check in game whether they need a row too.

## Change this container

- **Remove the row here only:** delete the `modifications` entry from `furnace_screen.json`. The row then doesn't appear on this screen, and nothing else changes.
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

- **The row is missing:** the path in `furnace_screen.json` no longer matches the game's vanilla tree. Compare the path with the current vanilla UI (see [19 — Hooking a vanilla screen](../19-how-to-hook-a-vanilla-screen.md)).
- **The row overlaps a vanilla control:** check the order in the hook (`insert_front` puts it on top, `insert_back` puts it below).
- **The screen is blank:** run `python3 tools/validate_pack.py pack`, then check the JSON for a missing comma.

## Status

The pack adds the management row, and the furnace guide panel built from [guides 01](../guides/01-furnace.md). The guide panel covers the tabs and items; the progress bars are not built yet (see [21 — Known issues](../21-known-issues-and-roadmap.md)).
