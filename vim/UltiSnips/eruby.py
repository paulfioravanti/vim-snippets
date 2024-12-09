"""
Companion python file for `eruby.snippets` file.
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
