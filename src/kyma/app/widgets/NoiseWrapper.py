from textual.app import ComposeResult
from textual.containers import Vertical
from textual.reactive import reactive
from textual.widgets import Label

from kyma.app.widgets import ControlBar, NoiseView


class NoiseWrapper(Vertical):
    """Vertical Wrapper of all things Noise Generating.

    ## Children:
        - NoiseView`
        - ControlBar
        - Label | FPS Counter

    """

    ## TODO: Really no way to inherti color "below"?
    DEFAULT_CSS = """
        #fps {
            position: absolute;
            offset: 1 1;
            color: yellow;
            background: transparent;
            layer: top;
        }
    """

    playing = reactive(False)

    def on_mount(self) -> None:
        self.watch(self.app, "config", self._refresh)

    def _refresh(self, config) -> None:
        fps = self.query_one("#fps", Label)
        fps.display = config.show_fps

    def compose(self) -> ComposeResult:
        yield NoiseView().data_bind(playing=NoiseWrapper.playing)
        yield ControlBar()
        yield Label("FPS: 0", id="fps")

    def toggle_play(self) -> None:
        self.playing = not self.playing

    def on_noise_view_fps_message(self, evt) -> None:
        fps = self.query_one("#fps", Label)
        if fps.display:
            fps.update(f"FPS: {evt.fps:.2f}")
