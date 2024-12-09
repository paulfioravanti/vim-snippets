"""
Companion python file for `elixir.snippets` file.
"""

from typing import Match


def struct_name(match: Match) -> str:
    """
    Construct and return a struct name for a match.
    """
    capture = match.group(1)
    return capture.lstrip().title() if capture else "Struct"

def tuple_tag(match: Match) -> str:
    """
    Tuple tag name helper.
    """
    tag = match.group(1)
    return "ok" if tag == "okay" else tag
