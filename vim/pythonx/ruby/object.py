"""
Companion python file for `ruby/object.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

from typing import Match


def method_or_proc(match: Match):
    """
    Determine whether to provide default text for a method or proc based on
    match object data.
    """
    return "." if match.group(1) == "." else " &"
