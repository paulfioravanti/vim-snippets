"""
Elm-related Ultisnips snippet helper functions.
NOTE: Changes to this file require restarting Vim!
"""

def flags_text(tabstop: str) -> str:
    """
    Return default text for flags
    """
    match tabstop:
        case "Flags":
            return "flags"
        case "()":
            return "()"
        case _:
            return "flags"
