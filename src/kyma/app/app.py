from dataclasses import replace

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.widgets import Input

from kyma.app.keybinds import KEYBINDS
from kyma.app.widgets import Legend, NoiseView, SummaryBar
from kyma.data import ConfigOptions, NoiseParams


class KymaApp(App):
    CSS_PATH = "global.tcss"

    # TODO: Try to remove if possible
    params = reactive(NoiseParams)
    config = reactive(ConfigOptions)

    def __init__(self, params, config):
        super().__init__()

        self.params = params
        self.config = config

    BINDINGS = [  # noqa: RUF012
        Binding(bind["key"], bind["action"], bind["desc"]) for bind in KEYBINDS
    ]

    def compose(self) -> ComposeResult:

        with Horizontal():
            with Vertical():
                yield SummaryBar()
                yield NoiseView()

            yield Legend()

    def on_input_submitted(self, evt: Input.Submitted):
        if evt.input.id == "scale":
            self.params = replace(self.params, scale=float(evt.value))

    ## Actions ##
    ## TODO: Move / Refactor
    ## Debounce? Performance issues on held

    def action_scale(self, delta):

        BOUNDS = (0, 10)
        self.params = replace(
            self.params,
            scale=round(min(BOUNDS[1], max(BOUNDS[0], self.params.scale + delta)), 2),
        )

    def action_toggle_debug(self):
        self.config = replace(self.config, show_value=not self.config.show_value)
