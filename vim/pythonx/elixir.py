"""
Companion python file for `elixir.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

from typing import Match


def struct_name(match: Match) -> str:
    """
    Construct and return a struct name for a match.
    """
    capture: str = match.group(1)
    return capture.lstrip().title() if capture else "Struct"

def tuple_tag(match: Match) -> str:
    """
    Tuple tag name helper.
    """
    tag: str = match.group(1)
    return "ok" if tag == "okay" else tag
