from dataclasses import replace

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive

from kyma.app.keybinds import KEYBINDS
from kyma.app.widgets import Legend, NoiseView, SummaryBar
from kyma.data import ConfigOptions, NoiseParams, NoiseParamsSpec


class KymaApp(App):
    CSS_PATH = "global.tcss"
    # TODO: App wide:
    # Notifications self.app.notify

    # TODO: Try to remove if possible
    params = reactive(NoiseParams)
    config = reactive(ConfigOptions)

    BINDINGS = [  # noqa: RUF012
        Binding(bind["key"], bind["action"], bind["desc"]) for bind in KEYBINDS
    ]

    def __init__(self, params, config):
        super().__init__()

        self.params = params
        self.config = config

    def compose(self) -> ComposeResult:

        with Horizontal():
            with Vertical():
                yield SummaryBar()
                yield NoiseView()

                # TODO: Controls widget. Play/Pause, Scrub, FPS, Speed

            yield Legend()

    ## Messages? ##

    ## TODO: horrid name
    def on_noise_view_fps_message(self, evt):
        self.query_one(SummaryBar).fps = evt.fps

    ## Actions ##

    def action_toggle_play(self):
        self.config = replace(self.config, playing=not self.config.playing)

    def action_change_fps(self, delta):
        new = self.config.fps + delta
        self.config = replace(self.config, fps=max(1, new))

    def action_change_speed(self, delta):
        self.config = replace(self.config, speed=self.config.speed + delta)

    ## TODO: Hacky
    ## TODO: App is still technically owning the data.
    ## Move bounds checking / updating into core app and pass through data?
    ## TOOD: Make this also work with config options
    def action_change(
        self,
        field,
        inverse=False,
        delta=None,
    ):
        meta = NoiseParamsSpec[field].metadata

        if delta is None:
            delta = meta["step"]

        if inverse:
            delta *= -1

        cur = getattr(self.params, field)
        new = round(min(meta["upper"], max(meta["lower"], cur + delta)), 3)

        self.params = replace(self.params, **{field: new})

    def action_reset(self, field=None):
        if field:
            default = NoiseParamsSpec[field].default
            self.params = replace(self.params, **{field: default})
        else:
            self.params = NoiseParams()

    def action_toggle_debug(self):
        self.config = replace(self.config, show_value=not self.config.show_value)
