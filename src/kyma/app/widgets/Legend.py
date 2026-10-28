from textual.app import ComposeResult
from textual.widgets import Label, Rule, Static

from kyma.app.keybinds import KEYBINDS


class Legend(Static):
    """Custom Legend Widget. (In-Progress).

    Uses the custom defined `KEYBINDS` list to construct a legend / key map.
    Similar to Textuals own `KeyPanel`, so could very well be redundant.

    TODO: Collapsible / Scrollable
    Or even a toggle between grouped / flat rendering
    """

    def compose(self) -> ComposeResult:
        groups = dict()
        for bind in KEYBINDS:
            groups.setdefault(bind.group, []).append(bind)

        ## TODO: Better formatting
        for name, binds in groups.items():
            yield Label(name)
            yield Rule()
            for bind in binds:
                key = bind.key
                if bind.display is not None:
                    key = bind.display

                yield Label(f"{key} {bind.desc}")
