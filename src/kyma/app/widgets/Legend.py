from textual.app import ComposeResult
from textual.widgets import Label, Rule, Static

from kyma.app.keybinds import KEYBINDS


# TODO: Collapsible / Scrollable
# Or even a toggle between grouped / flat rendering
class Legend(Static):
    def compose(self) -> ComposeResult:
        groups = dict()
        for bind in KEYBINDS:
            groups.setdefault(bind["group"], []).append(bind)

        ## TODO: Better formatting
        for name, binds in groups.items():
            yield Label(name)
            yield Rule()
            for bind in binds:
                key = bind["key"]
                if bind["display"] != "":
                    key = bind["display"]

                yield Label(f"{key} {bind['desc']}")

        ## TODO: Look into how styles work
        ## Hoping local scoped styles like Astro
