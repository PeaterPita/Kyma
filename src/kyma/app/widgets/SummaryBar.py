from rich.align import Align
from rich.panel import Panel
from textual.widgets import Static


class SummaryBar(Static):
    def on_mount(self):
        self.watch(self.app, "params", self._refresh)
        self.watch(self.app, "config", self._refresh)

    def _refresh(self, _):

        params = self.app.params  # pyright: ignore[reportAttributeAccessIssue]
        config = self.app.config  # pyright: ignore[reportAttributeAccessIssue]

        # seed = f"SEED: {user_seed}"
        # size = f"SIZE: {height} x {width}"
        sca = f"SCL: {params.scale}"
        otv = f"OCT: {params.octaves}"
        per = f"PER: {params.persistence}"
        lac = f"LAC: {params.lacunarity}"

        val = f"VALUES: {'Shown' if config.show_value else 'Hidden'}"

        joined_text = " | ".join([sca, otv, per, lac, val])
        self.update(Panel(Align.center(joined_text), style="bold"))
