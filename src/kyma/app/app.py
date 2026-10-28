from dataclasses import replace

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.widgets import KeyPanel

from kyma.app.keybinds import KEYBINDS
from kyma.app.widgets import NoiseWrapper, SummaryBar
from kyma.data import ConfigOptions, NoiseParams


class KymaApp(App):
    CSS_PATH = "global.tcss"
    # TODO: App wide:
    # Notifications self.app.notify

    params = reactive(NoiseParams)
    config = reactive(ConfigOptions)

    BINDINGS = [bind.to_textual() for bind in KEYBINDS]  # noqa: RUF012

    def __init__(self, params, config):
        super().__init__()

        self.params = params
        self.config = config

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical():
                yield SummaryBar()
                yield NoiseWrapper()
            # yield Legend()
            yield KeyPanel()

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
