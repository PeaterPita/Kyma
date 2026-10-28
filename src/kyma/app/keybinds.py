"""Module for handling textual keybind creating and registering."""

from dataclasses import dataclass

from textual.binding import Binding

## TODO: Keys left to implement
## TODO: Size control keybinds. (Arrows).
# {
#     "group": "Controls",
#     "key": "t",
#     "display": "",
#     "action": "change_fps(1)",
#     "desc": "Increase Animation FPS",
# },
# {
#     "group": "Controls",
#     "key": "g",
#     "display": "",
#     "action": "change_fps(-1)",
#     "desc": "Reduce Animation FPS.",
# },
# {
#     # TODO: Implement Legend Toggle
#     "group": "General",
#     "key": "ctrl+L",
#     "display": "",
#     "action": "",
#     "desc": "Toggle Legend Display",
# },
# {
#     # TODO: Implement Fullscreen
#     "group": "General",
#     "key": "ctrl+F",
#     "display": "",
#     "action": "",
#     "desc": "Toggle Fullscreen",
# }


@dataclass
class Keybind:
    """Custom Keybind data class, for easy registering.

    Can be converted to a Texual Binding object through `to_textual()`

    """

    group: str
    key: str
    action: str
    desc: str
    display: str | None = None

    def to_textual(self) -> Binding:
        """Return a Textual Binding Object from the keybind definition."""
        return Binding(self.key, self.action, self.desc)


def param_binds_helper(
    field: str,
    inc_key: str,
    dec_key: str,
    reset_key: str | None = None,
    label: str | None = None,
) -> list[Keybind]:
    """Create Increment, Decrement, Reset style keybinds.

    ## Arguments
    - `field`       | The value variable to modify.
    - `inc_key`     | The key to bind incrementing to.
    - `dec_key`     | The key to bind decrementing to.
    - `reset_key`   | The key to bind resetting to.
    - `label`       | The displayed name of the variable.

    Returns a List of `Keybind`s. This list can then be *unpacked.


    """
    label = label or field

    binds = [
        Keybind(
            "Controls",
            inc_key,
            f"change({field!r})",
            f"Increase {label} Factor",
        ),
        Keybind(
            "Controls",
            dec_key,
            f"change({field!r}, 'True')",
            f"Decrease {label} Factor",
        ),
    ]

    if reset_key:
        binds.append(
            Keybind(
                "Controls",
                reset_key,
                f"reset({field!r})",
                f"Reset {label} Factor",
            ),
        )

    return binds


KEYBINDS = [
    ###############
    # Inc/DEC/Rst
    *param_binds_helper("scale", "q", "a", "z"),
    *param_binds_helper("octaves", "w", "s", "x"),
    *param_binds_helper("persistence", "e", "d", "c"),
    *param_binds_helper("lacunarity", "r", "f", "v"),
    #########
    # TODO: Remove
    # Speed
    Keybind("Controls", "y", "change_speed(0.1)", "Increase Speed of Animation"),
    Keybind("Controls", "h", "change_speed(-0.1)", "Decrease Speed of Animation"),
    ###########
    # General
    Keybind("General", "escape", "reset()", "Reset All"),
    Keybind("General", "space", "toggle_play()", "Toggle Animation Playing"),
    Keybind("Debug", "0", "toggle_debug()", "Show Values"),
    Keybind("Debug", "1", "toggle_fps()", "Render Calculated FPS"),
]
