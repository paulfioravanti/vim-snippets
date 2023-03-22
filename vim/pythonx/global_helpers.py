"""
Ultisnips snippet global helper functions. Intended for any language.
NOTE: Changes to this file require restarting Vim!
"""

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
    # `choice_tabstop` comes through as a string. If it starts with "1", then
    # a choice has not been made yet.
    return surround if choice_tabstop.startswith("1") else ""
