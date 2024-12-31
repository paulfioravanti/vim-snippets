"""
Companion python file for `plover.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

from typing import Match


# Cannot type hint a `snip`.
def maybe_ending_comma(snip):
    """
    Add a comma to the end of the snip if its filetype (`snip.ft`) is json.
    """
    return "," if snip.ft == "json" else ""

def plover_modifier(match: Match) -> str:
    """
    Change OPTION to ALT for Plover commands.
    """
    modifier: str = upcase_match(match)
    return "ALT" if modifier == "OPTION" else modifier

def upcase_match(match: Match) -> str:
    """
    Upcase the match text.
    """
    return match.group(1).upper()
