"""
Companion python file for `ruby.snippets` file.
"""

from typing import Match


_GLOBAL_START: str = "global"
_GLOBAL_END: str = "endglobal"
_INLINE_PYTHON_START: str = "`!p "
_INLINE_PYTHON_END: str = "`"
_SNIPPET_START: str = "snippet"
_SNIPPET_END: str = "endsnippet"

def maybe_visual_colon(tabstop: str) -> str:
    """
    Determine whether VISUAL definition requires a colon.
    """
    return ":" if tabstop else ""

def parse_snippet_action_name(match: Match):
    """
    Return a snippet action name based on English spelling.
    """
    action_name = match.group(1)
    if action_name == "preexpand":
        return "pre_expand"

    return action_name.replace(" ", "_")
