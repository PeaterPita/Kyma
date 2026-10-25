from dataclasses import replace

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive

from kyma.app.keybinds import KEYBINDS
from kyma.app.widgets import Legend, NoiseView, SummaryBar
from kyma.data import ConfigOptions, NoiseParams, NoiseParamsSpec


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
    ## Debounce? Performance issues on held

    ## TODO: Hacky
    ## TODO: App is still technically owning the data.
    ## Move bounds checking / updating into core app and pass through data?
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
