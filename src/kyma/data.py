from dataclasses import dataclass, field, fields, replace
from random import randint


def _param_helper(default, step, lower=0, upper=10):
    return field(
        default=default, metadata={"step": step, "lower": lower, "upper": upper}
    )


def generate_random_seed() -> int:
    """Generate a random seed."""
    return randint(0, 1000000)


## TODO: Better name
## TODO: Make Generic
## From APP.py: Make this also work with config options
class _Shared_Custom:
    def change(self, field, delta, inverse=False):
        meta = NoiseParamsSpec[field].metadata

        if delta is None:
            delta = meta["step"]

        if inverse:
            delta *= -1

        cur = getattr(self, field)
        new = round(min(meta["upper"], max(meta["lower"], cur + delta)), 3)

        return replace(self, **{field: new})  # pyright: ignore[reportArgumentType]

    def reset(self, field):

        if field:
            default = NoiseParamsSpec[field].default
            return replace(self, **{field: default})  # pyright: ignore[reportArgumentType]

        else:
            return type(self)()

    def toggle(self, field):
        return replace(self, **{field: not getattr(self, field)})  # pyright: ignore[reportArgumentType]


@dataclass
class NoiseParams(_Shared_Custom):
    seed: int = generate_random_seed()
    scale: float = _param_helper(0.1, 0.01)
    octaves: int = _param_helper(1, 1, 1, 10)
    persistence: float = _param_helper(0.5, 0.01, 0, 1)
    lacunarity: float = _param_helper(2.0, 0.01, 1)


NoiseParamsSpec = {f.name: f for f in fields(NoiseParams)}


# TODO: a ConfigSpec map might be needed so the same param helper could be used.
# This would simplify changing fps and speed, values.
@dataclass
class ConfigOptions:
    # TODO: Still need control to change gradient / preset
    preset: str = "VIBRANT RAINBOW"
    show_value: bool = False
    fps: int = 30
    speed: float = 0.1
