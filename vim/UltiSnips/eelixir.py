"""
Companion python file for `eelixir.snippets` file.
"""

def eex_placeholder(tag: str) -> str:
    """
    Return eex tag-dependent placeholder text for a snippet.
    """
    if tag == "%#":
        return "comment"
    if tag in ["%%", "%%="]:
        return "quotation"
    return "expression"
