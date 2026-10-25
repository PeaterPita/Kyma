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
