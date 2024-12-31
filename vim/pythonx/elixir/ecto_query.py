"""
Companion python file for `elixir/ecto_query.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

from typing import Match


def query_expression_name(match: Match) -> str:
    """
    Return a query expression name, making fixes for 'order'-related matches.
    """
    name = match.group(1)
    name = "order_by" if name in ("order", "order by") else name
    return name

def queryable_first_character(queryable: list[str]) -> str:
    """
    Return the first character of a query.
    """
    if queryable:
        return queryable[0].lower()
    return "x"

# Cannot type hint a `snip`.
def queryable_name(snip, match):
    """
    Determine queryable name based of `snip` or `match` information.
    """
    if queryable := snip.v.text or match.group(1):
        return queryable.title()
    return "Queryable"
