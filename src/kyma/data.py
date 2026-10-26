from dataclasses import dataclass, field, fields
from random import randint


def _param_helper(default, step, lower=0, upper=10):
    return field(
        default=default, metadata={"step": step, "lower": lower, "upper": upper}
    )


def generate_random_seed() -> int:
    """Generate a random seed."""
    return randint(0, 1000000)


@dataclass
class NoiseParams:
    seed: int = generate_random_seed()
    scale: float = _param_helper(0.1, 0.01)
    octaves: int = _param_helper(1, 1, 1, 10)
    persistence: float = _param_helper(0.5, 0.01, 0, 1)
    lacunarity: float = _param_helper(2.0, 0.01, 1)


NoiseParamsSpec = {f.name: f for f in fields(NoiseParams)}


@dataclass
class ConfigOptions:
    # TODO: Still need control to change gradient / preset
    preset: str = "VIBRANT RAINBOW"
    show_value: bool = False
