from dataclasses import dataclass, replace

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.widgets import Input

from kyma.app.widgets import Legend, NoiseView, SummaryBar
from kyma.core.generate import generate_random_seed

## Data ##


@dataclass
class NoiseParams:
    seed: int = generate_random_seed()
    scale: float = 0.1
    octaves: int = 1
    persistence: float = 0.5
    lacunarity: float = 2.0


@dataclass
class ConfigOptions:
    preset: str = "VIBRANT RAINBOW"
    show_value: bool = False


## App ##


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

    # TODO: Better Init of values
    params = reactive(NoiseParams())
    config = reactive(ConfigOptions())

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
