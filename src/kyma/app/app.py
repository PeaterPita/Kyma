from dataclasses import replace

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.widgets import Input

from kyma.app.widgets import Legend, NoiseView, SummaryBar
from kyma.data import ConfigOptions, NoiseParams


class KymaApp(App):
    CSS = """
        NoiseView {
            height: 1fr;
            content-align: center middle;
        }

        Legend {
            width: 35;
        }
    """

    # TODO: Try to remove if possible
    params = reactive(NoiseParams)
    config = reactive(ConfigOptions)

    def __init__(self, params, config):
        super().__init__()

        self.params = params
        self.config = config

    def compose(self) -> ComposeResult:

        with Horizontal():
            with Vertical():
                yield SummaryBar()
                yield NoiseView()

                yield Input(id="scale", value="0.1", type="number")

            yield Legend()

    def on_input_submitted(self, evt: Input.Submitted):
        if evt.input.id == "scale":
            self.params = replace(self.params, scale=float(evt.value))
