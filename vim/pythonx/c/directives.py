"""
Companion python file for `c/directives.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

# ~/.vim/pythonx/global_helpers.py
from global_helpers import (
    choice_tabstop_chosen,
    closing_character
)


def include_ending(opening: str) -> str:
    """
    Return closing character for an opening character if choice tabstop chosen.
    """
    return closing_character(opening) if choice_tabstop_chosen(opening) else ""
