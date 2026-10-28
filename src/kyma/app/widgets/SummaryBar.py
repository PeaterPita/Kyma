from rich.align import Align
from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Label, Static


class SummaryBar(Horizontal):
    """Summary Bar displaying information about the current generating paramaters.

    Displaying: `[seed, scale, octaves, persistence, lacunarity, show_value]`

    ### TODO:
        - Reformat
        - Add size {width} x {height} module
    """

    DEFAULT_CSS = """
        SummaryBar {
            height: auto;
            align: center middle;
            padding: 1 2;
        }

        #title {
            color: $accent;
        }

    """

    def on_mount(self):
        self.watch(self.app, "params", self._refresh)
        self.watch(self.app, "config", self._refresh)

    def compose(self) -> ComposeResult:
        yield Label("Kyma", id="title")
        yield Static(id="values")

    def _refresh(self, _):

        params = self.app.params  # pyright: ignore[reportAttributeAccessIssue]
        config = self.app.config  # pyright: ignore[reportAttributeAccessIssue]

        seed = f"SEED: {params.seed}"
        # size = f"SIZE: {height} x {width}"
        sca = f"SCL: {params.scale}"
        otv = f"OCT: {params.octaves}"
        per = f"PER: {params.persistence}"
        lac = f"LAC: {params.lacunarity}"

        val = f"VALUES: {'Shown' if config.show_value else 'Hidden'}"

        joined_text = " | ".join([seed, sca, otv, per, lac, val])
        self.query_one("#values", Static).update(Align.center(joined_text))
