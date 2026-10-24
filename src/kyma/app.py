from opensimplex import OpenSimplex
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Header, Static

from kyma.main import generate
from kyma.presets import preset_colours


class NoiseView(Static):
    def on_mount(self):

        preset_names = list(preset_colours.keys())
        selected_preset = preset_names[0]
        gradient = preset_colours[selected_preset]

        params = (
            OpenSimplex(seed=4),
            50,
            20,
            0.1,
            1,
            0.5,
            2.0,
            gradient,
            False,
        )

        frame = generate(*params)
        self.update(frame)


class Legend(Static):
    pass


class SummaryBar(Static):
    pass


class KymaApp(App):
    def compose(self) -> ComposeResult:
        yield Header()

        yield SummaryBar("Testing")
        with Horizontal():
            yield NoiseView()
            yield Legend()
