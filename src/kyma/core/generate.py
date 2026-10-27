import numpy as np
from opensimplex import OpenSimplex
from rich.segment import Segment
from rich.style import Style

from kyma.core.colour import new_colourise_value
from kyma.core.presets import preset_colours
from kyma.data import NoiseParams

STEPS = 128


def layered_noise_array(
    ox: OpenSimplex,
    width: int,
    height: int,
    t: float,
    scale: float,
    octaves: int,
    persistence: float,
    lacunarity: float,
) -> np.ndarray:
    """Generate layered simplex noise value."""
    total = np.zeros((height, width), dtype=np.float32)
    frequency = 1
    amplitude = 1
    max_value = 0  # Used for normalizing result to -1.0 to 1.0

    x = np.arange(width) * scale
    y = np.arange(height) * scale
    z = np.array([t], dtype=np.float32)

    for _ in range(octaves):
        map3 = ox.noise3array(x * frequency, y * frequency, z * frequency)

        layer = map3[0]
        total += layer * amplitude
        max_value += amplitude
        amplitude *= persistence
        frequency *= lacunarity

    return total / max_value


def generate(
    ox: OpenSimplex | None,
    params: NoiseParams,
    width: int,
    height: int,
    t: float,
):
    """Generate and display the noise grid."""
    if ox is None:
        # Shouldn't ever happen but who knows
        return

    noise_map = layered_noise_array(
        ox,
        width,
        height,
        t,
        scale=params.scale,
        octaves=params.octaves,
        persistence=params.persistence,
        lacunarity=params.lacunarity,
    )

    index = np.rint((noise_map + 1.0) * 0.5 * (STEPS - 1))
    return np.clip(index, 0, STEPS - 1).astype(np.uint8)


def gen_color_table(preset, show_value):
    segments = []
    for v in np.linspace(-1.0, 1.0, STEPS):
        colour = new_colourise_value(float(v), preset_colours[preset])

        # TODO: Look into half block rendering
        # Could use `▀` symbols to "double" vertical resolution
        text = f" {v:+.2f} " if show_value else "██"
        segments.append(Segment(text, Style.parse(colour)))

    return segments
