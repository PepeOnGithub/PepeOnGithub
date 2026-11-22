# 22 — Glossary

| Term | Meaning |
|---|---|
| **Binding** | A link between a property on one control and a property or collection on another. See [05](05-json-ui-concepts.md). |
| **Control** | Any UI element: a panel, label, image, button, or toggle. A control is a JSON object with a `type`. |
| **Factory** | A template that builds one slot for one potion or ingredient. See [12](12-brewing-factories-and-potions.md). |
| **Flag** | A `#__is_<name>_key` property that tells the brewing guide which potion an item is. |
| **Hook** | A `modifications` entry in a vanilla override file that adds or removes pack controls in a vanilla screen. See [19](19-how-to-hook-a-vanilla-screen.md). |
| **Instance** | A control that inherits from a template with `@`. |
| **Lang key** | A `key=value` line in `texts/*.lang`, used as `%key` in UI JSON. See [16](16-localization.md). |
| **Modification** | An entry in a `modifications` array. It changes an existing control instead of defining a new one. |
| **Namespace** | The name that a file's controls are referenced by, written as `namespace.control`. Pack namespaces start with `bc_`. |
| **Nine-slice** | A texture stretched in a way that keeps its corners and borders sharp. Set with `$*_nineslice`. |
| **Property** | Runtime state on a control, written as `#name` (for example `#visible`). |
| **Radio** | A toggle that belongs to a group, where only one toggle in the group can be checked. |
| **Template** | A control reused with `@`, usually declaring `$variables` with defaults. See [06](06-template-catalog.md). |
| **Toggle** | A control with checked and unchecked states. |
| **Variable** | A value written as `$name`. Set per instance, or globally in `_global_variables.json`. |
| **Vanilla** | The game's own UI and textures. Pack files can hook into vanilla, but they don't ship vanilla content. |
