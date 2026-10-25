## TODO: Replace with dataclass with defaults

KEYBINDS = [
    #######################################
    {
        "group": "Controls",
        "key": "=",
        "display": "+",
        "action": "scale(0.1)",
        "desc": "Increase Scale Factor",
    },
    {
        "group": "Controls",
        "key": "-",
        "display": "",
        "action": "scale(-0.1)",
        "desc": "Decrease Scale Factor",
    },
    ######################################
    {
        "group": "Controls",
        "key": "q",
        "display": "",
        "action": "octaves()",
        "desc": "Increase Octave Count",
    },
    {
        "group": "Controls",
        "key": "a",
        "display": "",
        "action": "octaves()",
        "desc": "Decrease Octave Count",
    },
    #######################################
    {
        "group": "Controls",
        "key": "w",
        "display": "",
        "action": "persistence()",
        "desc": "\\[PH]",
    },
    {
        "group": "Controls",
        "key": "s",
        "display": "",
        "action": "persistence()",
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
