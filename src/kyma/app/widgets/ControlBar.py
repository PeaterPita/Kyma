from rich.align import Align
from rich.panel import Panel
from textual.app import ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Button, Label, ProgressBar, Select, Static


# TODO: Controls widget. Play/Pause, Scrub, FPS, Speed
class ControlBar(Horizontal):
    """Control Bar Widget. Allows play/pause of the animation, target fps, and speed."""

    DEFAULT_CSS = """
        ControlBar {
            height: auto;
        }
    """

    def compose(self) -> ComposeResult:
        yield Label(Align.center("[PH] Control Bar"))

        # yield Button()
        # yield Select(options=[("Test", 1), ("Hello", 2)])
        # yield ProgressBar()
        # yield Button()
        # yield Button()
