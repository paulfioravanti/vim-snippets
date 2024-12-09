"""
Companion python file for `html.snippets` file.
"""

from typing import Match

# ~/.vim/pythonx/javascript_helpers.py
from javascript_helpers import (
    class_attribute_name
)

# ~/.vim/pythonx/html_helpers.py
from html_helpers import (
    extract_ids_and_classes,
    text_to_tag
)


_MULTILINE = "multi-line"

# Cannot type hint a `snip`.
def build_tag_with_attributes(snip, match):
    """
    Dynamic HTML tag builder.
    """
    tag, attributes, tag_type = match.group(1, 2, 3)
    tag = text_to_tag(tag)
    # NOTE: Although a tag with attributes probably doesn't need this wrapping
    # $1 tabstop, without it, the snippet spacing is borked, which seems like a
    # bug in UltiSnips. Might be related to the following issue:
    # https://github.com/SirVer/ultisnips/issues/1013
    output = f"<{tag}${{1:"

    if attributes:
        ids, classes = extract_ids_and_classes(attributes)

        if ids:
            output += f" id=\"{ids}\""

        if classes:
            output += f" {class_attribute_name()}=\"{classes}\""
    else:
        output += "${2: id=\"${3:id}\"}"
        output += f"${{4: ${{5:{class_attribute_name()}}}=\"${{6:classes}}\"}}"

    output += "}$7>"

    visual = snip.context["visual"].strip(" \t\n\r")
    if tag_type == _MULTILINE:
        output += f"\n  ${{8:{visual}}}\n"
    else:
        output += f"${{8:{visual}}}"

    output += f"</{tag}>"
    snip.expand_anon(output)

def tag_args(match: Match) -> str:
    """
    Return tags for a match object.
    """
    return match.group(2) or ""
