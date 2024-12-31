"""
Companion python file for `javascript/import_export.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

import re


_OPENING_CURLY: str = "{ "


def import_module_text(tabstop: str) -> str:
    """
    Determine default text for import statement.
    """
    return (
        "exported"
        if re.match(rf"{_OPENING_CURLY}", tabstop)
        else "exported or *"
    )

def maybe_closing_import(tabstop: str) -> str:
    """
    Determine whether to close Javascript import statement with curly bracket.
    """
    return " }" if re.match(rf"{_OPENING_CURLY}", tabstop) else ""

def module_file_default_text(t1: str, t2: str) -> str:
    """
    Determine default text for modules in import statement.
    """
    if t2 in ["exported", "exported or *", "*"]:
        return "module"

    if t1:
        # NOTE: When the default text for t2 is deleted/changed, the tabstop
        # itself also seems to get deleted, and any replacement text is appended
        # to t1, hence this clause.
        file_text: str = t1.removeprefix(_OPENING_CURLY)
        return (
            f"./{file_text}"
            if file_text and file_text[0].isupper()
            else "module"
        )

    # NOTE: This clause will catch when the opening curly is deleted.
    return f"./{t2}"
