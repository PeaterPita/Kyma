"""Main module for generating and displaying 2D simplex noise in the terminal."""

from kyma.app.app import KymaApp


def main() -> None:

    # TOOD: Argument Parsing
    # Classic mode? Without textual
    # pass in color file
    # pass in noise params

    app = KymaApp()
    app.run()


if __name__ == "__main__":
    main()
