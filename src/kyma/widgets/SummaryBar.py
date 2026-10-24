from rich.align import Align
from rich.panel import Panel
from textual.widgets import Static


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
