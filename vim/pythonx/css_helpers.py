"""
CSS-related Ultisnips snippet helper functions.
NOTE: Changes to this file require restarting Vim!
"""

def join_properties(match: str) -> str:
    """
    Return joined properties together.
    """
    groups = [group for group in match.groups() if group is not None]
    return "-".join(groups)
