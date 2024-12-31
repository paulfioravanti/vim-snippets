"""
Companion python file for `ruby.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

from typing import Match

_PERCENT_LITERALS: dict[str, str] = {
    "string": "w",
    "word": "w",
    "symbol": "i"
}

# Cannot type hint a `snip`.
def initialize_args(tabstop, snip):
    """
    Dynamically initialize args for a Ruby class.
    """
    if not tabstop:
        snip.rv = ""
        return

    args = [string.strip() for string in tabstop.split(",") if string]
    snip.shift(2)
    for arg in args:
        snip += snip.mkline("", indent="")
        snip.rv += f"@{arg} = {arg}"

def initialize_attr_args(tabstop: str) -> str:
    """
    Dynamically initialize attr_* args for a Ruby class.
    """
    if not tabstop:
        return ""

    args = [string.strip() for string in tabstop.split(",") if string]
    attrs = map(lambda arg: f":{arg}", args)
    return " " + ", ".join(attrs)

def percent_literal(match: Match) -> str:
    """
    Convert word to percent literal character.
    """
    capture = match.group(1)
    if capture:
        return _PERCENT_LITERALS.get(capture, "")
    return ""

def words_to_constant(match: Match) -> str:
    """
    Convert words to a Ruby CONSTANT_NAME.
    """
    capture = match.group(1)
    if not capture:
        return "CONSTANT_NAME"

    word_list = capture.upper().split()
    return "_".join(word_list)
