from rich.align import Align
from rich.panel import Panel
from textual.widgets import Static


# TODO: Controls widget. Play/Pause, Scrub, FPS, Speed
class ControlBar(Static):
    """Control Bar Widget. Allows play/pause of the animation, target fps, and speed."""

    def on_mount(self):
        self.update(Panel(Align.center("[PH] Control Bar"), style="bold"))
