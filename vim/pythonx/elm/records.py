"""
Companion python file for `elm/records.snippets` file.
"""

from typing import Match


def field_value_default_text(field_name: str) -> str:
    """
    Return default value for an Elm record field.
    """
    return "value" if field_name == "fieldName" else field_name

def record_update_default_text(match: Match) -> str:
    """
    Return default value for an Elm record field during update.
    """
    return text if (text := match.group(1)) else "recordName"
