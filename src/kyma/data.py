from dataclasses import dataclass

from kyma.core.generate import generate_random_seed


@dataclass
class NoiseParams:
    seed: int = generate_random_seed()
    scale: float = 0.1
    octaves: int = 1
    persistence: float = 0.5
    lacunarity: float = 2.0


@dataclass
class ConfigOptions:
    preset: str = "VIBRANT RAINBOW"
    show_value: bool = False
