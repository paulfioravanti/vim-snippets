"""
Companion python file for `elm/html.snippets` file.
"""

from typing import (
    Match,
    cast
)

# ~/.vim/pythonx/html_helpers.py
from html_helpers import (
    extract_ids_and_classes,
    is_html_tag,
    text_to_tag
)


_DOUBLELINE: str = "double-line"
_MULTILINE: str = "multi-line"
_SINGLELINE: str = "single-line"

# Cannot type hint a `snip`.
# pylint: disable-next=too-many-branches
def build_tag_with_attributes(snip, match):
    """
    Builds a HTML tag with appropriate attributes.
    """
    tag, attributes, tag_type = match.group(1, 2, 3)
    tag = text_to_tag(tag)
    # NOTE: Although a tag with attributes probably doesn't need this wrapping
    # $1 tabstop, without it, the snippet spacing is borked, which seems like a
    # bug in UltiSnips.
    output = tag

    if tag_type == _MULTILINE:
        output += "\n   "

    output += " [ ${1:"

    if attributes:
        ids, classes = extract_ids_and_classes(attributes)

        if ids:
            output += f" id \"{ids}\""

            if classes:
                if tag_type == _MULTILINE:
                    output += "\n    "

                output += ","

        if classes:
            output += f" class \"{classes}\""
    else:
        output += "${2: id \"${3:id}\""
        if tag_type == _MULTILINE:
            output += "\n    ,}${4: class \"${6:classes}\""
        else:
            output += ",}${4: class \"${6:classes}\"}"

    if tag_type == _MULTILINE:
        output += "\n    "

        if not attributes:
            output += "}"

        output += "}$7 ]"
    else:
        output += "$7} ]"

    if tag_type == _SINGLELINE:
        output += " "
    else:
        output += "\n    "

    # NOTE: Unfortunately, visual text is not available in post_jump, so no
    # support for it can be provided.
    # See: https://github.com/SirVer/ultisnips/issues/1524
    if tag_type == _MULTILINE:
        output += "[ $8\n    ]"
    else:
        output += "[ $8 ]"

    snip.expand_anon(output)

def is_elm_html_tag(tag_name: str) -> bool:
    """
    Determines whether tag name is valid for Elm.
    """
    # NOTE: This handling needed due to:
    # - `main` being a valid HTML tag name but also an important Elm keyword
    # - `style` not being a valid tag for the Elm Html package; `style` is only
    # used as an attribute in Html.Attributes
    if tag_name in ["main", "style"]:
        return False

    if tag_name == "main_":
        return True

    return cast(bool, is_html_tag(tag_name))

def tag_args(match: Match) -> str:
    """
    Grab tag arguments from a match object.
    """
    return match.group(2) or ""
