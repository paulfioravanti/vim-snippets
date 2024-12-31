"""
Companion python file for `elm/types.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

from typing import Match

# ~/.vim/pythonx/global_helpers.py
from global_helpers import (
    words_to_pascal_case
)


def type_alias_default_text(text: str) -> str:
    """
    Determine default text for an Elm type alias.
    """
    return words_to_pascal_case(text) if text else "TypeAliasName"

def type_name_default_text(match: Match) -> str:
    """
    Determine default text for an Elm type name.
    """
    if match.group(1) in ["message", "msg"]:
        return "Msg"

    if (name := match.group(2)):
        return words_to_pascal_case(name)

    return "TypeName"
