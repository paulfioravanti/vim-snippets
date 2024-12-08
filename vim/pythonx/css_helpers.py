"""
CSS-related Ultisnips snippet helper functions.
NOTE: Changes to this file require restarting Vim!
"""

from typing import Match


def join_properties(match: Match) -> str:
    """
    Return joined properties together.
    """
    groups = [group for group in match.groups() if group is not None]
    return "-".join(groups)
