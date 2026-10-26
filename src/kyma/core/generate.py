import numpy as np
from opensimplex import OpenSimplex
from rich.text import Text

from kyma.core.colour import new_colourise_value
from kyma.core.presets import preset_colours
from kyma.data import ConfigOptions, NoiseParams


def layered_noise_array(
    ox: OpenSimplex,
    width: float,
    height: float,
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

    for _ in range(octaves):
        layer = ox.noise2array(x * frequency, y * frequency)
        total += layer * amplitude
        max_value += amplitude
        amplitude *= persistence
        frequency *= lacunarity

    return total / max_value


### params
# scale: float,
# octaves: int,
# persistence: float,
# lacunarity: float,
# gradient: list,
# show_value: bool,


## TODO: Optimise. Return np array. Handle rich text in app
## ^ Return just the values. Let the application perform the rendering. Eliminates the need for passing in config
def generate(
    ox: OpenSimplex | None,
    params: NoiseParams,
    config: ConfigOptions,
    width: int,
    height: int,
):
    """Generate and display the noise grid."""

    if ox is None:
        # Shouldn't ever happen but who knows
        return

    noise_map = layered_noise_array(
        ox,
        width,
        height,
        scale=params.scale,
        octaves=params.octaves,
        persistence=params.persistence,
        lacunarity=params.lacunarity,
    )

    frame = Text()
    for i in range(height):
        for j in range(width):
            noise_value = noise_map[i][j]
            colour = new_colourise_value(noise_value, preset_colours[config.preset])

            if not config.show_value:
                frame.append(
                    "██",
                    style=colour,
                )
            else:
                frame.append(f"[{noise_value:+.2f}]", style=colour)

        # New line after each row
        frame.append("\n")

    return frame
