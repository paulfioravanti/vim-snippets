"""
Companion python file for `c/control_flow.snippets` file.
"""

def maybe_block_end(tabstop: str) -> str:
    """
    Ends a block if the tabstop has opened one.
    """
    return "\n  }" if tabstop == " {" else ""
