"""
Python-related Ultisnips snippet helper functions.
NOTE: Changes to this file require restarting Vim!
"""

# ~/.vim/pythonx/global_helpers.py
from global_helpers import (
    snake_to_camel
)


# Cannot type hint a `snip`.
def class_name(snip):
    """
    Convert snippet file basename to camel case.
    """
    return snake_to_camel(snip.basename)
