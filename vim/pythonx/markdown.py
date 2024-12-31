"""
Companion python file for `markdown.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

from typing import Match

# ~/.vim/pythonx/global_helpers.py
from global_helpers import (
    choice_tabstop_chosen
)

def emphasis_ending(opening: str) -> str:
    """
    Return markdown emphasis ending character depending on the state of a choice
    tabstop.
    """
    return opening if choice_tabstop_chosen(opening) else ""

def heading(match: Match) -> str:
    """
    Dynamic Markdown heading tag generator.
    """
    return "#" * int(match.group(1))
