from opensimplex import OpenSimplex
from textual.widgets import Static

from kyma.main import generate


class NoiseView(Static):
    def on_mount(self):
        self.watch(self.app, "noiseParams", self._refresh)

    def _refresh(self, params):

        ox = OpenSimplex(seed=4)

        frame = generate(ox, params, 70, 50)
        self.update(frame)
