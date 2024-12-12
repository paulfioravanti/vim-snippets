"""
Companion python file for `elm/imports.snippets` file.
"""


def import_exposing_default_text(tabstop: str) -> str:
    """
    Return default text for Elm import exposing (...) statement.
    """
    return tabstop.split(".")[-1]

def module_alias_default_text(tabstop: str) -> str:
    """
    Return text for Elm module aliasing.
    """
    module_parts = tabstop.split(".")

    if len(module_parts) == 1:
        return "Alias"

    return text if (text := module_parts[-1]) else "Alias"
