"""Main module for generating and displaying 2D simplex noise in the terminal."""

import argparse
import sys
from dataclasses import fields

import numpy as np
from opensimplex import OpenSimplex

from kyma.app.app import KymaApp
from kyma.core.presets import preset_colours
from kyma.data import ConfigOptions, NoiseParams


# TODO: Classic mode? Without textual
# TODO: pass in color file
def parse_args():
    parser = argparse.ArgumentParser()

    for cls in (NoiseParams, ConfigOptions):
        for field in fields(cls):
            if "step" not in field.metadata:
                continue

            parser.add_argument(
                f"--{field.name}",
                help=f"Startup {field.name} Value"
                + (" (default: %(default)s)" if field.name != "seed" else ""),
                type=(type(field.default)),
                metavar="",
                default=(field.default),
            )

    parser.add_argument(
        "--preset",
        help="Set the color gradient to one of the presets.",
        type=str.upper,
        metavar="",
        choices=preset_colours,
    )

    parser.add_argument(
        "--list-presets",
        action="store_true",
        help="Show all preset colour options",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.list_presets:
        for preset in preset_colours:
            print(f"  - {preset}")
        sys.exit(0)

    params = NoiseParams.create_from_args(args)
    config = ConfigOptions.create_from_args(args)

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
