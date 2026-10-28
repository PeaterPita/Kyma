<div align="center">
    <picture> 
        <img alt="Kyma - Banner" src="assets/banner-dark.svg"/>
    </picture>
    <p> A Tool to visualise simplex noise in a command-line interface.
</div>

---

> [!NOTE]
> This is a seriously simple project.
>
> Forked from: [TheUsernameIsNotLong/simplex-noise-visualiser](https://github.com/TheUsernameIsNotLong/simplex-noise-visualiser)


## Installation


1. Clone this repository to your local device:
```bash 
git clone https://github.com/PeaterPita/Kyma.git 
cd Kyma 
```


> [!WARNING]
> `Numba` seems to be causing the program to crash occasionally. 
>
> On my machine this was mitigated by adding a "warm up" invocation to OpenSimplex in the main. 
> However this seems highly unstable. 
>
> Run `uv remove numba` if you encounter issues. However, performance will be **severely** degraded.


2. Run 
```bash 
uv run kyma
```


## Usage 

```bash 
usage: kyma [-h] [--scale ] [--octaves ] [--persistence ] [--lacunarity ] [--fps ] [--speed ] [--preset ] [--list-presets]

options:
  -h, --help      show this help message and exit
  --scale         Startup scale Value (default: 0.1)
  --octaves       Startup octaves Value (default: 1)
  --persistence   Startup persistence Value (default: 0.5)
  --lacunarity    Startup lacunarity Value (default: 2.0)
  --fps           Startup fps Value (default: 30)
  --speed         Startup speed Value (default: 0.1)
  --preset        Set the color gradient to one of the presets.

  --list-presets  Show all preset colour options
```





## Development 

<details> 
<summary>Nix Users</summary>
The supplied flake.nix contains a dev-shell providing the correct python and uv versions. Enter the shell through: 


```bash
nix develop
```

</details>

This project uses [UV](https://docs.astral.sh/uv/) as its python package manager. As such ensure your development environment is synced to the versions pinned in the lock file:
```bash 
uv sync
```


