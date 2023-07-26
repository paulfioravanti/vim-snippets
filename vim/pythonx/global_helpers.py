"""
Ultisnips snippet global helper functions. Intended for multiple languages.
NOTE: Changes to this file require restarting Vim!
"""

_CLOSING_CHARACTERS = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
    "|": "|",
    ":": ":",
    "`": "`",
    "\"": "\""
}

def choice_tabstop_chosen(choice_tabstop):
    """
    Checks if a choice tabstop has been chosen.
    """
    # `choice_tabstop` comes through as a string. If it starts with "1.", then
    # a choice has not been made yet.
    return not choice_tabstop.startswith("1.")

def closing_character(tabstop):
    """
    Return closing character for a tabstop containing an opening character.
    """
    # Just in case there are empty strings directly after the tabstop, making
    # them run into each other, always take the first character of the string.
    return _CLOSING_CHARACTERS.get(tabstop[0], "") if tabstop else ""

def key_closing(opening):
    """
    Intended for languages that have key-value stores where their keys can be
    written as both strings or some kind of constant (like an atom or symbol
    etc). E.g.
    {"foo" => bar}
    {foo: bar}
    """
    return "\" =>" if opening == "\"" else ":"

def maybe(tabstop, alternative):
    """
    A simple maybe clause to put in an alternative value if a tabstop
    is missing.
    """
    return "" if tabstop else alternative

def maybe_comma(left, right):
    """
    Aims to remove commas between function arguments when the right-side
    argument is removed.
    """
    return ", " if left and right else ""

def maybe_surround(choice_tabstop, surround):
    """
    Surround a choice tabstop with `surround` chars to indicate the whole
    tabstop itself is optional.
    """
    return "" if choice_tabstop_chosen(choice_tabstop) else surround

def snake_to_camel(string):
    """
    Given a snake_cased_string, returns a CamelCaseString.
    """
    return string.replace("_", " ").title().replace(" ", "")

def words_to_camel_case(words):
    """
    Converts words into a camelCase string for use as a function name.
    """
    head, *tail = words.split(" ")
    tail = [word.capitalize() for word in tail]
    return "".join([head, *tail])

def visual_context(snip):
    """
    Visual text is not available in post_jump by default
    (see: https://github.com/SirVer/ultisnips/issues/1524), so this function
    works around that limitation by storing the visual text inside a context
    dictionary, which can then be accessed during post_jump.
    Context blocks are not just for conditional statements, they can store
    actual context state.
    See html.snippets for an example of using this function.
    """
    return {"visual": snip.visual_text}
