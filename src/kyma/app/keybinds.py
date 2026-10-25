## TODO: Replace with dataclass with defaults

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
