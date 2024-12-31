"""
Companion python file for `elm/platform.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

def effect_module_name(string: str) -> str:
    """
    Determine Elm effect module name.
    """
    return "Cmd" if string.startswith(("C", "c")) else "Sub"
