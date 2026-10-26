from opensimplex import OpenSimplex
from textual.widgets import Static

from kyma.core.generate import generate


class NoiseView(Static):
    def on_mount(self):
        self.watch(self.app, "params", self._refresh)
        self.watch(self.app, "config", self._refresh)

    def _refresh(self, _):
        params = self.app.params  # pyright: ignore[reportAttributeAccessIssue]
        config = self.app.config  # pyright: ignore[reportAttributeAccessIssue]

        ox = OpenSimplex(seed=params.seed)

        frame = generate(ox, params, config, 70, 50)
        self.update(frame)
