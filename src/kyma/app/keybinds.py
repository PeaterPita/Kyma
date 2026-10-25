## TODO: Replace with dataclass with defaults

KEYBINDS = [
    #######################################
    {
        "group": "Controls",
        "key": "q",
        "display": "",
        "action": "scale(0.01)",
        "desc": "Increase Scale Factor",
    },
    {
        "group": "Controls",
        "key": "a",
        "display": "",
        "action": "scale(-0.01)",
        "desc": "Decrease Scale Factor",
    },
    ######################################
    {
        "group": "Controls",
        "key": "w",
        "display": "",
        "action": "octaves(1)",
        "desc": "Increase Octave Count",
    },
    {
        "group": "Controls",
        "key": "s",
        "display": "",
        "action": "octaves(-1)",
        "desc": "Decrease Octave Count",
    },
    #######################################
    {
        "group": "Controls",
        "key": "e",
        "display": "",
        "action": "persistence(0.01)",
        "desc": "\\[PH]",
    },
    {
        "group": "Controls",
        "key": "d",
        "display": "",
        "action": "persistence(-0.01)",
        "desc": "\\[PH]",
    },
    #######################################
    {
        "group": "Controls",
        "key": "r",
        "display": "",
        "action": "lacunarity(0.1)",
        "desc": "\\[PH]",
    },
    {
        "group": "Controls",
        "key": "f",
        "display": "",
        "action": "lacunarity(-0.1)",
        "desc": "\\[PH]",
    },
    #######################################
    {
        "group": "General",
        "key": "L",
        "display": "",
        "action": "",
        "desc": "Toggle Legend Display",
    },
    {
        "group": "General",
        "key": "F",
        "display": "",
        "action": "",
        "desc": "Toggle Fullscreen",
    },
    {
        "group": "Debug",
        "key": "0",
        "display": "",
        "action": "toggle_debug()",
        "desc": "Show Values",
    },
]
