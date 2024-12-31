"""
Companion python file for `elixir/phoenix_html.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

_OPENING_EEX_TAG: str = "<%"
_OPENING_EVAL_EEX_TAG: str = "<%="
_CLOSING_EEX_TAG: str = "%>"

# Cannot type hint a `snip`.
def do_eex_tag(snip, t):
    """
    Determine whether closing eex tag is needed after a `do`.
    """
    return f" {_CLOSING_EEX_TAG}" if _has_eex_context(snip) or t else ""

# Cannot type hint a `snip`.
def final_eex_tag(snip, t):
    """
    Determine whether closing eex tag is needed after an `end`.
    """
    return f" {_CLOSING_EEX_TAG}" if not _has_eex_context(snip) and t else ""

# Cannot type hint a `snip`.
def initial_eex_tag(snip):
    """
    Determine whether opening eex tag is needed before expression.
    """
    return f"{_OPENING_EVAL_EEX_TAG} " if not _has_eex_context(snip) else ""

# Cannot type hint a `snip`.
def initial_end_eex_tag(snip, t):
    """
    Determine whether opening eex tag is needed before an `end`.
    """
    return f"{_OPENING_EEX_TAG} " if _has_eex_context(snip) or t else ""

# Cannot type hint a `snip`.
def maybe_eex_tag(snip):
    """
    Put potential eex tag in snippet context.
    """
    return snip.before.lstrip()[0:3]

# Cannot type hint a `snip`.
def _has_eex_context(snip):
    return snip.context == _OPENING_EVAL_EEX_TAG
