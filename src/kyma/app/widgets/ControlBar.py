from rich.align import Align
from rich.panel import Panel
from textual.widgets import Static


# TODO: Controls widget. Play/Pause, Scrub, FPS, Speed
class ControlBar(Static):
    def on_mount(self):
        self.update(Panel(Align.center("[PH] Control Bar"), style="bold"))
