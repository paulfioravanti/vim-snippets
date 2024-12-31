"""
Companion python file for `elixir/phoenix.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

from typing import Match

# ~/.vim/pythonx/global_helpers.py
from global_helpers import (
    closing_character
)


def binding_var(match: Match, tabstop: str) -> str:
    """
    Return name for a binding variable.
    """
    return (
        _binding_name(match)
        + closing_character(tabstop)
        + _binding_assign_character(tabstop)
    )

def _binding_name(match: Match) -> str:
    return match.group(1).replace(" ", "-")

def _binding_assign_character(character: str) -> str:
    if character == "\"":
        return ": "
    return "="
