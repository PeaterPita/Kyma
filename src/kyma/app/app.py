# noqa: D100
from dataclasses import replace

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive

from kyma.app.keybinds import KEYBINDS
from kyma.app.widgets import Legend, NoiseWrapper, SummaryBar
from kyma.data import ConfigOptions, NoiseParams


class KymaApp(App):
    """Kyma: Textual-UI.

    ## TODO:
        - App wide Notifications (self.app.notify)


    """

    CSS_PATH = "global.tcss"

    params = reactive(NoiseParams)
    config = reactive(ConfigOptions)

    BINDINGS = [bind.to_textual() for bind in KEYBINDS]  # noqa: RUF012

    def __init__(self, params, config):  # noqa: D107
        super().__init__()

        self.params = params
        self.config = config

    def compose(self) -> ComposeResult:  # noqa: D102
        with Horizontal():
            with Vertical():
                yield SummaryBar()
                yield NoiseWrapper()
            yield Legend()

    ## Actions ##

    def action_toggle_play(self):
        self.query_one(NoiseWrapper).toggle_play()

    def action_change_fps(self, delta):
        new = self.config.fps + delta
        self.config = replace(self.config, fps=max(1, new))

    def action_change_speed(self, delta):
        self.config = self.config.change("speed", delta)

    def action_change(self, field, inverse=False, delta=None):
        self.params = self.params.change(field, delta, inverse)

    def action_reset(self, field=None):
        self.params = self.params.reset(field)

    def action_toggle_debug(self):
        self.config = self.config.toggle("show_value")

    def action_toggle_fps(self):
        self.config = self.config.toggle("show_fps")
