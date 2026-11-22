# 06 — Chest guide

The chest guide covers the chest and the double chest. The reference chest adds three things on top of the basic slots:
a **search box**, and **quick-transfer** controls for the chest and the inventory (named *stealer* in the reference file).

## Parts

| Part | Reference name | This pack today |
|---|---|---|
| Search box | `glacier_chest_search` (a text edit box) | Not built. The chest variables (`$search_field_*`) are present, so the box needs only a control. |
| Small chest quick-transfer | `small_chest_stealer` | Not built |
| Large chest quick-transfer | `large_chest_stealer`, `glacier_large_chest_stealer` | Not built |
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
