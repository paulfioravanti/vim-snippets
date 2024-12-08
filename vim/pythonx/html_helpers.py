"""
HTML-related Ultisnips snippet helper functions.
NOTE: Changes to this file require restarting Vim!
"""

import re
from typing import Pattern


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

def can_map_to_tag_name(string: str) -> bool:
    """
    Checks whether string can be mapped to a HTML tag.
    """
    return string in _TAG_NAME_MAPPINGS

def extract_ids_and_classes(attributes: str) -> tuple[str, str]:
    """
    Extract html ids and classes from a string of attributes.
    """
    return (
        _attribute_text(_IDS, attributes),
        _attribute_text(_CLASSES, attributes)
    )

def is_html_input_tag(string: str) -> re.Match[str] | None:
    """
    Checks whether string contains a HTML input tag with a known input type.
    """
    return re.match(_HTML_INPUT_TYPE_KEYWORD, string)

def is_html_min_max_input_tag(string: str) -> re.Match[str] | None:
    """
    Checks whether string contains a HTML input tag with a known input type.
    """
    return re.match(_HTML_MIN_MAX_INPUT_TYPE_KEYWORD, string)

def is_html_tag(string: str) -> re.Match[str] | None:
    """
    Checks whether string contains a known HTML tag.
    """
    return re.match(_HTML_TAG_KEYWORD, string)

def text_to_tag(text: str) -> str:
    """
    Returns HTML tag from English text or just the text if it cannot be mapped.
    """
    return _TAG_NAME_MAPPINGS.get(text, text)

def _attribute_text(attribute_type: Pattern, attributes: str) -> str:
    return " ".join(re.findall(attribute_type, attributes))
