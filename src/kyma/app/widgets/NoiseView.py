from opensimplex import OpenSimplex
from textual.widgets import Static

from kyma.core.generate import generate


class NoiseView(Static):
    def on_mount(self):
        self._last_seed = None
        self._ox = None

        self.watch(self.app, "params", self._refresh)
        self.watch(self.app, "config", self._refresh)

    def _refresh(self, _):
        params = self.app.params  # pyright: ignore[reportAttributeAccessIssue]
        config = self.app.config  # pyright: ignore[reportAttributeAccessIssue]

        # TODO: Debounce
        # THis is good. But still performance issues.
        # Instead of a debounce; render at capped rate
        if params.seed != self._last_seed:
            self._ox = OpenSimplex(seed=params.seed)
            self._last_seed = params.seed

        frame = generate(self._ox, params, config, 70, 50)
        self.update(frame)
