from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Label, Static


class Legend(Static):
    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label("Testing")
            yield Label("Hello")
