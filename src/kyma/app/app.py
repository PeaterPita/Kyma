from dataclasses import replace

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.widgets import Input

from kyma.app.keybinds import KEYBINDS
from kyma.app.widgets import Legend, NoiseView, SummaryBar
from kyma.data import ConfigOptions, NoiseParams


def normalise(value, bounds):
    return round(min(bounds[1], max(bounds[0], value)), 3)


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

    ## Actions ##
    ## TODO: Move / Refactor
    ## Debounce? Performance issues on held

    ## TODO: Change to one general action
    ## And add step and defaults to the dataclass fields. This is unmanageable

    def action_scale(self, delta):

        BOUNDS = (0, 10)
        self.params = replace(
            self.params, scale=normalise(self.params.scale + delta, BOUNDS)
        )

    def action_octaves(self, delta):

        BOUNDS = (1, 10)
        self.params = replace(
            self.params, octaves=normalise(self.params.octaves + delta, BOUNDS)
        )

    def action_persistence(self, delta):

        BOUNDS = (0, 1)
        self.params = replace(
            self.params, persistence=normalise(self.params.persistence + delta, BOUNDS)
        )

    def action_lacunarity(self, delta):

        BOUNDS = (1, 10)
        self.params = replace(
            self.params, lacunarity=normalise(self.params.lacunarity + delta, BOUNDS)
        )

    def action_toggle_debug(self):
        self.config = replace(self.config, show_value=not self.config.show_value)
