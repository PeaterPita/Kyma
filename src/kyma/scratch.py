def print_summary_bar(
    user_seed: int,
    height: int,
    width: int,
    scale: float,
    octaves: int,
    persistence: float,
    lacunarity: float,
):
    """Print a summary bar of the user's configuration."""
    seed = f"SEED: {user_seed}"
    size = f"SIZE: {height} x {width}"
    sca = f"SCL: {scale}"
    otv = f"OCT: {octaves}"
    per = f"PER: {persistence}"
    lac = f"LAC: {lacunarity}"
    joined_text = " | ".join([seed, size, sca, otv, per, lac])
    panel = Panel(Align.center(joined_text), style="bold", width=width * 2)

    # This wont align if show_value is true;
    # but since that dramatically increases width, this is acceptable
    console.print(panel)
