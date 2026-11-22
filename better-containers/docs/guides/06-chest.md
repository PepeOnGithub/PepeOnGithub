# 06 — Chest guide

## Status

Built: `ui/better_containers/containers/chest_guide.json`, hooked into the small and large chest after the overlay rows. It has a search box (the shared text box) and two buttons: Auto place all (`button.container_auto_place`) and Auto place one (`button.container_auto_place_one`). The search box filters the chest slots: the shared slot template (`bc_shared.input_panel_with_index`) hides any slot whose item name doesn't contain the text. It works because the text box exposes the name `utility_search_box`, which the template reads. The two button actions are the ones the pack's move buttons use; confirm in game that "Auto place all" does what its label says.

The chest guide covers the chest and the double chest. The reference chest adds three things on top of the basic slots:
a **search box**, and **quick-transfer** controls for the chest and the inventory (named *stealer* in the reference file).

## Parts

| Part | Reference name | This pack today |
|---|---|---|
| Search box | `glacier_chest_search` (a text edit box) | Built: `chest_guide` search box filters the slots |
| Small chest quick-transfer | `small_chest_stealer` | Covered by the Auto place all button (the same action the pack's move buttons use) |
| Large chest quick-transfer | `large_chest_stealer`, `glacier_large_chest_stealer` | Covered by the Auto place all button |
| Overlay rows (move, drop) | row overlays | Built (see [containers 01](../containers/01-chest.md)) |

The reference's "stealer" is a quick-transfer control. Check the exact action in game before you copy the behavior.

## Search box

A search box filters the visible items. It uses the shared text box (`bc_shared.text_edit_control`).
The pack's redstone screen already uses the same control (see [containers 13](../containers/13-redstone.md)).

## What to build

1. Add the search box to the chest's root, using the shared text box.
2. Add the quick-transfer controls for each chest size, using the chest's row templates.
3. Test that the search box doesn't close the screen when typing.

## Checklist

- [ ] Small and large chests both show the search box
- [ ] Typing filters the items
- [ ] Quick-transfer moves items in the expected direction
