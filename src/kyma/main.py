"""Main module for generating and displaying 2D simplex noise in the terminal."""

import argparse

import numpy as np
from opensimplex import OpenSimplex

from kyma.app.app import KymaApp
from kyma.core.presets import preset_colours
from kyma.data import ConfigOptions, NoiseParams, NoiseParamsSpec


# TODO: Classic mode? Without textual
# TODO: pass in color file
def parse_args():
    parser = argparse.ArgumentParser()

    for spec, field in NoiseParamsSpec.items():
        parser.add_argument(
            f"--{spec}",
            help=f"Startup {spec} Value"
            + (" (default: %(default)s)" if spec != "seed" else ""),
            type=(type(field.default)),
            metavar="",
            default=(field.default),
        )

    parser.add_argument(
        "--preset",
        help="Set the color gradient to one of the presets.",
        type=str.upper,
        choices=preset_colours,
        default="VIBRANT RAINBOW",
    )

    parser.add_argument(
        "--fps",
        help="Set the Target FPS of the noise animation",
        type=int,
        default=30,
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    arg_override = {}
    for spec in NoiseParamsSpec:
        args_val = getattr(args, spec)
        if args_val is not None:
            arg_override[spec] = args_val

    config_override = {}
    if args.preset:
        config_override["preset"] = args.preset

    if args.fps:
        config_override["fps"] = args.fps

    params = NoiseParams(**arg_override)
    config = ConfigOptions(**config_override)

    warm_numba()

    app = KymaApp(params=params, config=config)
    app.run()


if __name__ == "__main__":
    main()


## TODO: Program wide
## Work on Doc Strings and Type hinting


## TODO: this is required for some reason?
## Instant Crash occurs if numba is not used before textual uses it?
def warm_numba():
    ox = OpenSimplex(seed=0)
    ox.noise3array(np.arange(4) * 0.1, np.arange(4) * 0.1, np.array([0.0]))
