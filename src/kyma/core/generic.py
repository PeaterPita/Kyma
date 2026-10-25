"""Utility functions for getting user input with default values."""

from typing import TypeVar

T = TypeVar("T", int, float)


def get_number_input(
    prompt: str,
    default: T,
    upper: T | None = None,
    lower: T | None = None,
) -> T:
    """Get an integer or float input from the user, with a default value."""
    num_parser = type(default)

    while True:
        value = input(prompt)
        if value.strip() == "":
            return default

        try:
            parsed_value = num_parser(value)
            if upper is not None and parsed_value > upper:
                print(f"Please enter a value less than or equal to {upper}.")
            elif lower is not None and parsed_value < lower:
                print(f"Please enter a value greater than or equal to {lower}")
            else:
                return parsed_value

        except ValueError as err:
            print(f"Invalid input. Using default value of {default}.\nError: {err}")
            return default
