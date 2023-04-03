"""
Ultisnips snippet global helper functions. Intended for multiple languages.
NOTE: Changes to this file require restarting Vim!
"""

import vim

_CLOSING_CHARACTERS = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
    "|": "|",
    ":": ":",
    "\"": "\""
}

def closing_character(tabstop):
    """
    Return closing character for a tabstop containing an opening character.
    """
    if tabstop:
        return _CLOSING_CHARACTERS.get(tabstop[0], "")
    return ""

def key_closing(opening):
    """
    Intended for languages that have key-value stores where their keys can be
    written as both strings or some kind of constant (like an atom or symbol
    etc). E.g.
    {"foo" => bar}
    {foo: bar}
    """
    return "\" =>" if opening == "\"" else ":"

def choice_tabstop_chosen(choice_tabstop):
    """
    Checks if a choice tabstop has been chosen.
    """
    # `choice_tabstop` comes through as a string. If it starts with "1.", then
    # a choice has not been made yet.
    return not choice_tabstop.startswith("1.")

def jump_forward():
    """
    Jumps forward a tabstop.
    """
    # REF: https://github.com/reconquest/vim-pythonx/blob/master/pythonx/px/snippets.py#LL117C5-L118C41
    vim.command('call feedkeys("\<C-R>=UltiSnips#JumpForwards()\<CR>")')

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
    return surround if not is_chosen(choice_tabstop) else ""
