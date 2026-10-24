<div align="center">
    <h1>Kyma</h1>
    <p> A Tool to visuualise simplex noise in a command-line interface.
</div>

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

2. Run 
```bash 
uv run kyma
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


