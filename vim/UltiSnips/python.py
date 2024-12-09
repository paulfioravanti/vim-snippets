"""
Companion python file for `python.snippets` file.
"""

from typing import Match

def comprehension_opening(match: Match) -> str:
    """
    Return comprehension character opening dependent on type specified.
    """
    match match.group(1):
        case "list":
            return "["
        case "generator":
            return "("
        case _:
            return "{"
