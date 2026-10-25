"""Module for handling colour gradients and mapping noise values to colours."""

from math import ceil, floor

from rich.console import Console

console = Console()


def new_colourise_value(value: float, gradient: list) -> str:
    """Convert a noise value to a colored string for terminal output."""
    # Clamp value between -1 and 1
    clamped_value = max(-1, min(1, value))
    # Map value to a range encompassing all gradient points
    mapped_value = (len(gradient) * (clamped_value + 1)) / 2
    # Interpolate colour from custom values
    lower_colour = gradient[floor(mapped_value) - 1]  # 127, 255, 0
    upper_colour = gradient[ceil(mapped_value) - 1]  # 255, 0, 0

    modulo_value = mapped_value % 1
    r = int(lower_colour[0] + (upper_colour[0] - lower_colour[0]) * modulo_value)
    g = int(lower_colour[1] + (upper_colour[1] - lower_colour[1]) * modulo_value)
    b = int(lower_colour[2] + (upper_colour[2] - lower_colour[2]) * modulo_value)
    return f"rgb({r},{g},{b})"
