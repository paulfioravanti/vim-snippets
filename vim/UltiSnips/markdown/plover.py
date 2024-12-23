"""
Companion python file for `markdown/plover.snippets` file.
"""

from typing import Match

def star_flag_suffix(match: Match) -> str:
    """
    Extract star flag suffix from a match object if it exists.
    """
    suffix = match.group(1)
    return suffix or ""
