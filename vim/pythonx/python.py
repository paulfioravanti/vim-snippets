"""
Companion python file for all Python snippets.
NOTE: Changes to this file require restarting Vim!
"""

from typing import Match

# ~/.vim/pythonx/globals.py
from globals import (
    snake_to_camel
)


# Cannot type hint a `snip`.
def class_name(snip):
    """
    Convert snippet file basename to camel case.
    """
    return snake_to_camel(snip.basename)

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
