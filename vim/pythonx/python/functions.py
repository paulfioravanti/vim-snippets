"""
Companion python file for `python/functions.snippets` file.
"""

from typing import Match


def decorator_tag(match: Match) -> str:
    """
    Determine decorator tag name for a Python function.
    """
    return "classmethod" if "class" in match.group(1) else "staticmethod"
