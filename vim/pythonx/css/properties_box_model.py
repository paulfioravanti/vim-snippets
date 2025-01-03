"""
Companion python file for `css/properties_box_model.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

from typing import Match


def limit_length_property(match: Match) -> str:
    """
    Determine property name for a min/max height/width property.
    """
    limit: str
    property_type: str

    limit, property_type = match.group(1, 2)
    limit = limit.replace("imum", "")
    return f"{limit}-{property_type}"
