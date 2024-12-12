"""
Companion python file for `elm/platform.snippets` file.
"""

def effect_module_name(string: str) -> str:
    """
    Determine Elm effect module name.
    """
    return "Cmd" if string.startswith(("C", "c")) else "Sub"
