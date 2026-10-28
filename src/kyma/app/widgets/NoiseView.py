import time

from opensimplex import OpenSimplex
from textual.message import Message
from textual.reactive import reactive
from textual.strip import Strip
from textual.widget import Widget

from kyma.core.generate import gen_color_table, generate


## TODO: Centering
## Changing from Static to a Widget has caused NoiseView to no longer be centered
class NoiseView(Widget):
    playing = reactive(False)

    def on_mount(self):
        self._last_seed = None
        self._ox = None

        # Time / Animation Stuff
        self._timer = None
        self._start = time.monotonic()

        self.t = 0.0
        self._marked = True

        self.fps = 0
        self._frames = 0
        self._busy_time = 0.0

        # Rendering
        self._frame = None
        self._colour_table = []
        self._last_render_key = None

        # Watchers
        self.watch(self.app, "params", self._mark)
        self.watch(self.app, "config", self._conf_changed)

    def _conf_changed(self, config):
        config_fps = config.fps

        ## TODO: Switch from timers to threaded tick worker
        if config_fps != self.fps:
            self.fps = config_fps

            if self._timer:
                self._timer.stop()

            self._timer = self.set_interval(1 / self.fps, self._tick)

        self._mark(None)

    def _mark(self, _):
        self._marked = True

    def _tick(self):
        config = self.app.config  # pyright: ignore[reportAttributeAccessIssue]
        now = time.monotonic()

        dt = now - self._start
        self._start = now

        if self.playing:
            self.t += dt * config.speed
            self._marked = True

        if not self._marked:
            return

        self._marked = False

        self._refresh()
        self._frames += 1
        self._busy_time += dt

        if self._busy_time >= 0.5:
            fps = self._frames / self._busy_time

            self._frames = 0
            self._busy_time = 0

            self.post_message(self.FpsMessage(fps))

    def render_line(self, y):
        frame = self._frame
        table = self._colour_table

        if frame is None or table is None or y >= frame.shape[0]:
            return Strip.blank(self.size.width)

        return Strip([table[i] for i in frame[y].tolist()])

    def _refresh(self):
        params = self.app.params  # pyright: ignore[reportAttributeAccessIssue]
        config = self.app.config  # pyright: ignore[reportAttributeAccessIssue]

        if params.seed != self._last_seed:
            self._ox = OpenSimplex(seed=params.seed)
            self._last_seed = params.seed

        render_key = (config.preset, config.show_value)
        if render_key != self._last_render_key:
            self._last_render_key = render_key
            self._colour_table = gen_color_table(*render_key)

        ## TODO: Hard coded size still needs changing
        frame = generate(self._ox, params, 70, 50, self.t)
        if frame is None:
            return

        self._frame = frame
        self.refresh()

    class FpsMessage(Message):
        def __init__(self, fps: float):
            self.fps = fps
            super().__init__()
