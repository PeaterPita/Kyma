from textual.app import ComposeResult
from textual.containers import Vertical
from textual.reactive import reactive
from textual.widget import Widget

from kyma.app.widgets import ControlBar, NoiseView


class NoiseWrapper(Widget):
    playing = reactive(False)

    def compose(self) -> ComposeResult:
        with Vertical():
            yield NoiseView().data_bind(playing=NoiseWrapper.playing)
            yield ControlBar()

    def toggle_play(self):
        self.playing = not self.playing
