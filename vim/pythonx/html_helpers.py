import re


_HTML_TAG_KEYWORDS = [
    "article",
    "audio",
    "body",
    "button",
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
    "ordered list",
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
    "unordered list",
    "var",
    "video"
]
HTML_TAG_KEYWORD = re.compile(rf"\b({'|'.join(_HTML_TAG_KEYWORDS)})\b")

_HTML_INPUT_TYPE_KEYWORDS = [
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
HTML_INPUT_TYPE_KEYWORD = re.compile(
    rf"\b({'|'.join(_HTML_INPUT_TYPE_KEYWORDS)})\b"
)

_HTML_MIN_MAX_INPUT_TYPE_KEYWORDS = ["date", "number", "range"]
HTML_MIN_MAX_INPUT_TYPE_KEYWORD = re.compile(
    rf"\b({'|'.join(_HTML_MIN_MAX_INPUT_TYPE_KEYWORDS)})\b"
)

IDS = re.compile(r"(?<=#)[^\.#]+") # #some-id
CLASSES = re.compile(r"(?<=\.)[^\.#]+") # .some-class

# Bridging list of English words/phrases to HTML tag names
TAG_NAME_MAPPINGS = {
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
    "ruby text": "rt",
    "sample": "samp",
    "table data": "td",
    "table footer": "tfoot",
    "table head": "thead",
    "table row": "tr",
    "text area": "textarea",
    "unordered list": "ul"
}
