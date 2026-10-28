from textual.app import ComposeResult
from textual.containers import Vertical
from textual.reactive import reactive
from textual.widget import Widget

from kyma.app.widgets import ControlBar, NoiseView


class NoiseWrapper(Vertical):
    playing = reactive(False)

    def compose(self) -> ComposeResult:
        with Vertical():
            yield NoiseView().data_bind(playing=NoiseWrapper.playing)
            yield ControlBar()

    def toggle_play(self):
        self.playing = not self.playing

    ## TODO: FPS Overlay
    # def on_noise_view_fps_message(self, evt):
    #     self.query_one(SummaryBar).fps = evt.fps
