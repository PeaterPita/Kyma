from textual.app import ComposeResult
from textual.widgets import Label, Rule, Static

# TODO: Compose actual bindings, lengend, and summary bar all from the same list
GROUPS = [
    ("SCALE (SCL)", "↑ / ↓"),
    ("OCTAVES (OCT)", "< / >"),
    ("PERSISTENCE (PER)", "W / S"),
]

GENERAL = [
    ("Space", "play / pause"),
    ("L", "Toggle Legned"),
    ("F", "Toggle Fullscreen"),
    ("Q", "Quit"),
]


DEBUG = [("V", "Show Values")]


class Legend(Static):
    def compose(self) -> ComposeResult:
        yield Label("Controls")
        yield Rule()

        ## TODO: Look into how styles work
        ## Hoping local scoped styles like Astro

        for title, hint in GROUPS:
            yield Label(title)
            yield Label(hint)

        yield Rule()
        yield Label("General")

        for title, hint in [*GENERAL, *DEBUG]:
            yield Label(f"{title} {hint}")
