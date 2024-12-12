"""
Companion python file for `elm/control_flow.snippets` file.
"""

from typing import Match

def case_variable_default_text(match: Match, default: str) -> str:
    """
    Determine default text for a `case` variable.
    """
    return text.strip() if (text := match.group(1)) else default
