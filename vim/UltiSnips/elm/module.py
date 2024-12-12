"""
Companion python file for `elm/module.snippets` file.
"""

def module_exposing_default_text(tabstop: str) -> str:
    """
    Return default text for Elm's module exposing.
    """
    return "main" if tabstop == "Main" else ".."
