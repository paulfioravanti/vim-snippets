"""
Companion python file for `eruby.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

def erb_placeholder(tag: str) -> str:
    """
    Return place holder for opening erb tag.
    """
    if tag == "%#":
        return "comment"

    if tag == "%==":
        return "raw_expression"

    return "expression"
