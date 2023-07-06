"""
Elm-related Ultisnips snippet helper functions.
NOTE: Changes to this file require restarting Vim!
"""

# ~/.vim/pythonx/global_helpers.py
from global_helpers import (
    choice_tabstop_chosen
)


def flags_text(tabstop):
    """
    Return default text for flags
    """
    if not choice_tabstop_chosen(tabstop):
        return "flags"

    return tabstop.lower()

def maybe_flags(tabstop):
    """
    Return default flags text or remove argument
    """
    if not choice_tabstop_chosen(tabstop):
        return " flags"

    return "" if tabstop == "()" else f" {tabstop.lower()}"
