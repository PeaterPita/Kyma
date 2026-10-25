# def print_summary_bar(
#     user_seed: int,
#     height: int,
#     width: int,
#     scale: float,
#     octaves: int,
#     persistence: float,
#     lacunarity: float,
# ):
#     """Print a summary bar of the user's configuration."""
#     seed = f"SEED: {user_seed}"
#     size = f"SIZE: {height} x {width}"
#     sca = f"SCL: {scale}"
#     otv = f"OCT: {octaves}"
#     per = f"PER: {persistence}"
#     lac = f"LAC: {lacunarity}"
#     joined_text = " | ".join([seed, size, sca, otv, per, lac])
#     panel = Panel(Align.center(joined_text), style="bold", width=width * 2)
#
#     # This wont align if show_value is true;
#     # but since that dramatically increases width, this is acceptable
#     console.print(panel)
#
#
# def initialise():
#     # 3: Miscellanous display settings
#     print(
#         "Would you like to use a preset colour gradient or create your own? (default 1)"
#     )
#     print("1. Preset")
#     print("2. Custom")
#     choice = get_number_input("Enter choice (1-2): ", 1)
#     if choice == 1:
#         print("Available presets:")
#         for i, preset_name in enumerate(preset_colours.keys(), start=1):
#             console.print(f"{i}. {preset_name}")
#         preset_choice = get_number_input("Select a preset by number (default 1): ", 1)
#         preset_names = list(preset_colours.keys())
#         selected_preset = preset_names[preset_choice - 1]
#         gradient = preset_colours[selected_preset]
#     else:
#         gradient_points = get_number_input(
#             "Enter number of gradient points (default 2): ", 2
#         )
#         gradient = determine_gradient_points(gradient_points)
#
#     try:
#         show_value = str(input("Show noise values? (y/N): ")).strip().lower() == "y"
#         if not show_value:
#             show_value = False
#     except ValueError:
#         show_value = False
#
#
# Genric.py

# """Utility functions for getting user input with default values."""
#
# from typing import TypeVar
#
# T = TypeVar("T", int, float)
#
#
# ## Redundant unless keeping a "classic" mode
# def get_number_input(
#     prompt: str,
#     default: T,
#     upper: T | None = None,
#     lower: T | None = None,
# ) -> T:
#     """Get an integer or float input from the user, with a default value."""
#     num_parser = type(default)
#
#     while True:
#         value = input(prompt)
#         if value.strip() == "":
#             return default
#
#         try:
#             parsed_value = num_parser(value)
#             if upper is not None and parsed_value > upper:
#                 print(f"Please enter a value less than or equal to {upper}.")
#             elif lower is not None and parsed_value < lower:
#                 print(f"Please enter a value greater than or equal to {lower}")
#             else:
#                 return parsed_value
#
#         except ValueError as err:
#             print(f"Invalid input. Using default value of {default}.\nError: {err}")
#             return default


# def determine_gradient_points(num_points: int):
#     """Determine key gradient colours for noise mapping."""
#     gradient_points = []
#     # Loop to get RGB values for each gradient point
#     for i in range(num_points):
#         r = get_number_input(
#             f"Enter red value (0-255) of point {i + 1}/{num_points}: ",
#             255,
#             upper=255,
#             lower=0,
#         )
#         g = get_number_input(
#             f"Enter green value (0-255) of point {i + 1}/{num_points}: ",
#             255,
#             upper=255,
#             lower=0,
#         )
#         b = get_number_input(
#             f"Enter blue value (0-255) of point {i + 1}/{num_points}: ",
#             255,
#             upper=255,
#             lower=0,
#         )
#         console.print(f"Gradient point {i + 1} set.", style=f"rgb({r},{g},{b})")
#         gradient_points.append([r, g, b])
#     return gradient_points
#
#
#
