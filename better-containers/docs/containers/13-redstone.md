# 13 — Redstone containers

The vanilla `redstone_screen` is hooked in two places, `panel/root_panel/redstone_screen_inventory` and
`panel_crafter/root_panel/redstone_screen_inventory`. The two paths suggest two variants of one screen: a plain one and a
crafter one. Confirm in game which block opens each variant before you change it.

## At a glance

| Field | Value |
|---|---|
| Vanilla screen | Redstone screen (plain variant and crafter variant) |
| File | `ui/redstone_screen.json` (vanilla override, keep the name) |
| Hook paths | `panel/root_panel/redstone_screen_inventory`, `panel_crafter/root_panel/redstone_screen_inventory` |
| Operation | `insert_front` into `controls` |
| Inserted control | `bc_shared.redstone_content` |

## What the pack adds

`redstone_content` is a shared panel in `shared/shared_controls.json`. It holds two things:

- the **management row** (`right_elements`, which uses `primary_management_toggles` with `$toggle_position: right`), and
- a **search text box** (`text_box`, built from `bc_shared.text_edit_control`).

So each redstone variant gets the management row and a search box together.

## Change this container

- **Change both variants at once:** edit `redstone_content` in `shared_controls.json`.
- **Change one variant only:** remove that path's `modifications` entry and add a new one with the content you want.
- **Remove the search box:** delete `text_box` from `redstone_content`, which also affects any other user of that control.

## Testing checklist

- [ ] The plain redstone screen shows the management row and search box
- [ ] The crafter variant shows the same
- [ ] Typing in the search box works and does not close the screen
- [ ] The management toggles work on both variants

## Troubleshooting

- **Only one variant shows the row:** check both hook paths, since they are separate entries.
- **The search box covers slots:** adjust the anchor or offset in `redstone_content`.

## Status

Both variants use the same shared content, so changes here stay consistent. The exact vanilla block for each path is not checked in this repo.
