# https://github.com/reconquest/vim-pythonx
import px.snippets
from px.snippets import (
    advance_jumper,
    get_jumper_position,
    get_jumper_text
)

def autojump_if_blank(snip, positions):
    """
    Derived from the "Autojump from tabstop when it's empty" guide:
    https://github.com/SirVer/ultisnips/tree/master/doc/examples/autojump-if-empty
    """
    if (
        get_jumper_position(snip) in positions and
        not get_jumper_text(snip)
    ):
        advance_jumper(snip)

def make_context(snip):
    """
    Wrapper around px.snippets method.
    """
    return px.snippets.make_context(snip)

def make_jumper(snip, on_tabstop=1):
    """
    Wrapper around px.snippets method.
    """
    return px.snippets.make_jumper(snip, on_tabstop)
