"""
Companion python file for `javascript/react.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

import re
from typing import Pattern


_PROP_SPACES_KEEP_END_BRACKET: Pattern = re.compile(r"\s(?![^{]*\})|(/?>$)")
_ON_PROP: Pattern = re.compile(r"^on([A-Z]\w+)")

# Cannot type hint a `snip`.
def format_tag(snip):
    """
    Formats a React tag.
    """
    parts = list(
        filter(None, re.split(_PROP_SPACES_KEEP_END_BRACKET, snip.v.text))
    )
    snip.rv += parts[0]
    for part in parts[1:-1]:
        snip += snip.mkline("", indent="  ")
        snip.rv += part
    snip += snip.mkline("", indent="")
    snip.rv += parts[-1]

def maybe_self_closing(tabstop: str) -> str:
    """
    Determines whether to self-close a React tag
    """
    return "" if tabstop else " /"

def prop_value_placeholder(tabstop: str) -> str:
    """
    Determines placeholder value for a React prop.
    """
    if (match := _ON_PROP.match(tabstop)):
        return "handle" + match.group(1)

    return tabstop

# Cannot type hint a `snip`.
def state_text_defaults(snip, tabstop):
    """
    Determines placeholder values for useState function.
    """
    state_name = _uppercased(tabstop) or "State"
    set_state_text = f"set{state_name}"
    initial_state_text = snip.v.text or f"initial{state_name}"
    return (set_state_text, initial_state_text)

def _uppercased(tabstop: str) -> str:
    return tabstop[0].capitalize() + tabstop[1:] if tabstop else ""
