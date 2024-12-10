"""
Companion python file for `css/selectors.snippets` file.
"""

from typing import Match

def selector_info(match: Match) -> tuple[str, str]:
    """
    Return CSS selector info from a word.
    """
    selector_type: str = match.group(1)
    match selector_type:
        case "class":
            return (".", selector_type)
        case "id":
            return ("#", selector_type)
        case _:
            return ("", selector_type)
