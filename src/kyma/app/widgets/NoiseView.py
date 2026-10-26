import time

from opensimplex import OpenSimplex
from textual.widgets import Static

from kyma.core.generate import generate

# TODO: Move to config
# No idea how variable FPS is going to work. Reset interval timing?
FPS = 1 / 30
SPEED = 0.1


class NoiseView(Static):
    def on_mount(self):
        self._last_seed = None
        self._ox = None

        # Time / Animation Stuff
        self.t = 0.0
        self._start = time.monotonic()
        self._marked = True

        self.watch(self.app, "params", self._mark)
        self.watch(self.app, "config", self._mark)
        self.set_interval(FPS, self._tick)

    def _mark(self, _):
        self._marked = True

    def _tick(self):
        config = self.app.config  # pyright: ignore[reportAttributeAccessIssue]

        now = time.monotonic()

        dt = now - self._start
        self._start = now

        if config.playing:
            self.t += dt * SPEED
            self._marked = True

        if not self._marked:
            return

        self._marked = False

        ## TODO: Remove config requirement. This is temp
        self._refresh(config)

    def _refresh(self, config):
        params = self.app.params  # pyright: ignore[reportAttributeAccessIssue]

        if params.seed != self._last_seed:
            self._ox = OpenSimplex(seed=params.seed)
            self._last_seed = params.seed

        frame = generate(self._ox, params, config, 70, 50, self.t)
        if frame is None:
            return
        self.update(frame)
