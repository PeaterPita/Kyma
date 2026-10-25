"""Main module for generating and displaying 2D simplex noise in the terminal."""

from kyma.app.app import KymaApp
from kyma.data import ConfigOptions, NoiseParams


def main() -> None:

    # TODO: Argument Parsing
    # Classic mode? Without textual
    # pass in color file
    # pass in noise params

    params = NoiseParams(scale=1.33)
    config = ConfigOptions()

    app = KymaApp(params=params, config=config)
    app.run()


if __name__ == "__main__":
    main()
