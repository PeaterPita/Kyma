# Split widgets into seperate files
from opensimplex import OpenSimplex
from rich.align import Align
from rich.panel import Panel
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.reactive import reactive
from textual.widgets import Input, Static

from kyma.main import generate
from kyma.presets import preset_colours


class NoiseView(Static):
    def on_mount(self):
        self.watch(self.app, "noiseParams", self._refresh)

    def _refresh(self, params):

        ox = OpenSimplex(seed=4)

        frame = generate(ox, params, 70, 50)
        self.update(frame)


class Legend(Static):
    pass


class SummaryBar(Static):
    def on_mount(self):
        self.watch(self.app, "noiseParams", self._refresh)

    def _refresh(self, params):
        # seed = f"SEED: {user_seed}"
        # size = f"SIZE: {height} x {width}"
        sca = f"SCL: {params['scale']}"
        otv = f"OCT: {params['octaves']}"
        per = f"PER: {params['persistence']}"
        lac = f"LAC: {params['lacunarity']}"
        joined_text = " | ".join([sca, otv, per, lac])
        self.update(Panel(Align.center(joined_text), style="bold"))


class KymaApp(App):
    preset_names = list(preset_colours.keys())
    selected_preset = preset_names[0]

    # TODO: Replace with data class
    # TODO: Split gradient and show values. Theyre not params
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
