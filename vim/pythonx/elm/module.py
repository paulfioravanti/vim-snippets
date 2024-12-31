"""
Companion python file for `elm/module.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

def module_exposing_default_text(tabstop: str) -> str:
    """
    Return default text for Elm's module exposing.
    """
    return "main" if tabstop == "Main" else ".."
