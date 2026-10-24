# Split widgets into seperate files
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.reactive import reactive
from textual.widgets import Input

from kyma.presets import preset_colours
from kyma.widgets import Legend, NoiseView, SummaryBar


class KymaApp(App):
    preset_names = list(preset_colours.keys())
    selected_preset = preset_names[0]

    # TODO: Replace with data class
    # TODO: Split gradient and show values. Theyre not params
    # TODO: Better Init of values

    noiseParams = reactive(
        {
            "scale": 0.1,
            "octaves": 1,
            "persistence": 0.5,
            "lacunarity": 2.0,
            "gradient": preset_colours[selected_preset],
            "show_value": False,
        }
    )

    def compose(self) -> ComposeResult:
        yield SummaryBar("Testing")
        yield Input(id="scale", value="0.1", type="number")
        with Horizontal():
            yield NoiseView()
            yield Legend()

    def on_input_submitted(self, evt: Input.Submitted):
        if evt.input.id == "scale":
            self.noiseParams = {**self.noiseParams, "scale": float(evt.value)}
