"""
Companion python file for all HTML snippets.
NOTE: Changes to this file require restarting Vim!
"""

import re
from typing import (
    Match,
    Pattern
)

# ~/.vim/pythonx/javascript.py
from javascript import (
    class_attribute_name
)


_HTML_TAG_KEYWORDS: list[str] = [
    "article",
    "audio",
    "blockquote",
    "body",
    "button",
    "cite",
    "code",
    "div",
    "em",
    "figcaption",
    "figure",
    "footer",
    "form",
    "h[1-6]",
    "head",
    "html",
    "kbd",
    "li",
    "main",
    "nav",
    "ol",
    "p(?:re)?",
    "rt",
    "ruby",
    "samp",
    "section",
    "select",
    "span",
    "strong",
    "style",
    "table",
    "tbody",
    "td",
    "textarea",
    "tfoot",
    "th",
    "title",
    "tr",
    "ul",
    "var",
    "video"
]
_HTML_TAG_KEYWORD: Pattern = (
    re.compile(rf"\b({'|'.join(_HTML_TAG_KEYWORDS)})\b")
)

_HTML_INPUT_TYPE_KEYWORDS: list[str] = [
    "button",
    "checkbox",
    "color",
    "datetime-local",
    "email",
    "file",
    "hidden",
    "month",
    "password",
    "radio",
    "reset",
    "search",
    "submit",
    "text",
    "time",
    "url",
    "week",
]
_HTML_INPUT_TYPE_KEYWORD: Pattern = re.compile(
    rf"\b({'|'.join(_HTML_INPUT_TYPE_KEYWORDS)})\b"
)

_HTML_MIN_MAX_INPUT_TYPE_KEYWORDS: list[str] = ["date", "number", "range"]
_HTML_MIN_MAX_INPUT_TYPE_KEYWORD: Pattern = re.compile(
    rf"\b({'|'.join(_HTML_MIN_MAX_INPUT_TYPE_KEYWORDS)})\b"
)

_IDS: Pattern = re.compile(r"(?<=#)[^\.#]+") # #some-id
_CLASSES: Pattern = re.compile(r"(?<=\.)[^\.#]+") # .some-class

# Bridging list of English words/phrases to HTML tag names
_TAG_NAME_MAPPINGS: dict[str, str] = {
    "block quote": "blockquote",
    "figure caption": "figcaption",
    "heading 1": "h1",
    "heading 2": "h2",
    "heading 3": "h3",
    "heading 4": "h4",
    "heading 5": "h5",
    "heading 6": "h6",
    "keyboard": "kbd",
    "list item": "li",
    "ordered list": "ol",
    "paragraph": "p",
    "ruby text": "rt",
    "sample": "samp",
    "table data": "td",
    "table footer": "tfoot",
    "table head": "thead",
    "table row": "tr",
    "text area": "textarea",
    "unordered list": "ul"
}

_MULTILINE = "multi-line"

def can_map_to_tag_name(string: str) -> bool:
    """
    Checks whether string can be mapped to a HTML tag.
    """
    return string in _TAG_NAME_MAPPINGS

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

def extract_ids_and_classes(attributes: str) -> tuple[str, str]:
    """
    Extract html ids and classes from a string of attributes.
    """
    return (
        _attribute_text(_IDS, attributes),
        _attribute_text(_CLASSES, attributes)
    )

def is_html_input_tag(string: str) -> Match[str] | None:
    """
    Checks whether string contains a HTML input tag with a known input type.
    """
    return re.match(_HTML_INPUT_TYPE_KEYWORD, string)

def is_html_min_max_input_tag(string: str) -> Match[str] | None:
    """
    Checks whether string contains a HTML input tag with a known input type.
    """
    return re.match(_HTML_MIN_MAX_INPUT_TYPE_KEYWORD, string)

def is_html_tag(string: str) -> Match[str] | None:
    """
    Checks whether string contains a known HTML tag.
    """
    return re.match(_HTML_TAG_KEYWORD, string)

def tag_args(match: Match) -> str:
    """
    Return tags for a match object.
    """
    return match.group(2) or ""

def text_to_tag(text: str) -> str:
    """
    Returns HTML tag from English text or just the text if it cannot be mapped.
    """
    return _TAG_NAME_MAPPINGS.get(text, text)

def _attribute_text(attribute_type: Pattern, attributes: str) -> str:
    return " ".join(re.findall(attribute_type, attributes))
