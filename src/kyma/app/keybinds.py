## TODO: Replace with dataclass with defaults
## TODO: Helper for general Inc, Dec, Reset binds
## TODO: Size control keybinds. (Arrows)

KEYBINDS = [
    #######################################
    {
        "group": "Controls",
        "key": "q",
        "display": "",
        "action": "change('scale')",
        "desc": "Increase Scale Factor",
    },
    {
        "group": "Controls",
        "key": "a",
        "display": "",
        "action": "change('scale', True)",
        "desc": "Decrease Scale Factor",
    },
    {
        "group": "Controls",
        "key": "z",
        "display": "",
        "action": "reset('scale')",
        "desc": "Reset scale value to default",
    },
    ######################################
    {
        "group": "Controls",
        "key": "w",
        "display": "",
        "action": "change('octaves')",
        "desc": "Increase Octave Count",
    },
    {
        "group": "Controls",
        "key": "s",
        "display": "",
        "action": "change('octaves', True)",
        "desc": "Decrease Octave Count",
    },
    {
        "group": "Controls",
        "key": "x",
        "display": "",
        "action": "reset('octaves')",
        "desc": "Reset Octaves value to default",
    },
    #######################################
    {
        "group": "Controls",
        "key": "e",
        "display": "",
        "action": "change('persistence')",
        "desc": "\\[PH]",
    },
    {
        "group": "Controls",
        "key": "d",
        "display": "",
        "action": "change('persistence', True)",
        "desc": "\\[PH]",
    },
    {
        "group": "Controls",
        "key": "c",
        "display": "",
        "action": "reset('persistence')",
        "desc": "Reset Persistence value to default",
    },
    #######################################
    {
        "group": "Controls",
        "key": "r",
        "display": "",
        "action": "change('lacunarity')",
        "desc": "\\[PH]",
    },
    {
        "group": "Controls",
        "key": "f",
        "display": "",
        "action": "change('lacunarity', True)",
        "desc": "\\[PH]",
    },
    {
        "group": "Controls",
        "key": "v",
        "display": "",
        "action": "reset('lacunarity')",
        "desc": "Reset Lacunarity value to default",
    },
    #######################################
    {
        "group": "General",
        "key": "escape",
        "display": "",
        "action": "reset()",
        "desc": "Reset All",
    },
    {
        # TODO: Implement Legend Toggle
        "group": "General",
        "key": "ctrl+L",
        "display": "",
        "action": "",
        "desc": "Toggle Legend Display",
    },
    {
        # TODO: Implement Fullscreen
        "group": "General",
        "key": "ctrl+F",
        "display": "",
        "action": "",
        "desc": "Toggle Fullscreen",
    },
    {
        "group": "General",
        "key": "space",
        "display": "Space",
        "action": "toggle_play()",
        "desc": "Toggle Anaimtion Playing",
    },
    {
        "group": "Debug",
        "key": "0",
        "display": "",
        "action": "toggle_debug()",
        "desc": "Show Values",
    },
]
