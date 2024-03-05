"""
CSS-related Ultisnips snippet helper functions.
NOTE: Changes to this file require restarting Vim!
"""

def join_properties(match):
    """
    Return joined properties together.
    """
    return "-".join(match.groups())
