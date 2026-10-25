from random import randint

import numpy as np
from opensimplex import OpenSimplex
from rich.text import Text

from kyma.core.colour import determine_gradient_points, new_colourise_value
from kyma.core.generic import get_number_input
from kyma.core.presets import preset_colours
from kyma.scratch import print_summary_bar


def generate_random_seed() -> int:
    """Generate a random seed."""
    return randint(0, 1000000)


def initialise():
    """Initialise settings by getting user input."""
    # 1: Seed value
    user_seed = get_number_input(
        "Enter a seed number (leave blank for a random value): ", generate_random_seed()
    )
    ox = OpenSimplex(seed=user_seed)

    # 2: Noise generation settings
    height = get_number_input(
        "Enter number of rows (default 20): ", 20, upper=1000, lower=1
    )
    width = get_number_input(
        "Enter number of columns (default 50): ", 50, upper=1000, lower=1
    )
    scale = get_number_input("Enter scale (default 0.1): ", 0.1, upper=10, lower=0)
    octaves = get_number_input(
        "Enter number of octaves (default 1): ", 1, upper=10, lower=1
    )
    persistence = get_number_input(
        "Enter persistence (default 0.5): ", 0.5, upper=1, lower=0
    )
    lacunarity = get_number_input(
        "Enter lacunarity (default 2.0): ", 2.0, upper=10, lower=1
    )

    # 3: Miscellanous display settings
    print(
        "Would you like to use a preset colour gradient or create your own? (default 1)"
    )
    print("1. Preset")
    print("2. Custom")
    choice = get_number_input("Enter choice (1-2): ", 1)
    if choice == 1:
        print("Available presets:")
        for i, preset_name in enumerate(preset_colours.keys(), start=1):
            console.print(f"{i}. {preset_name}")
        preset_choice = get_number_input("Select a preset by number (default 1): ", 1)
        preset_names = list(preset_colours.keys())
        selected_preset = preset_names[preset_choice - 1]
        gradient = preset_colours[selected_preset]
    else:
        gradient_points = get_number_input(
            "Enter number of gradient points (default 2): ", 2
        )
        gradient = determine_gradient_points(gradient_points)

    try:
        show_value = str(input("Show noise values? (y/N): ")).strip().lower() == "y"
        if not show_value:
            show_value = False
    except ValueError:
        show_value = False

    print_summary_bar(user_seed, height, width, scale, octaves, persistence, lacunarity)

    return (
        ox,
        height,
        width,
        scale,
        octaves,
        persistence,
        lacunarity,
        gradient,
        show_value,
    )


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


def generate(
    ox: OpenSimplex,
    params,
    config,
    width,
    height,
):
    """Generate and display the noise grid."""
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
