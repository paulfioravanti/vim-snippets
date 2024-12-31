"""
Companion python file for `elixir/phoenix_live_view.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

# ~/.vim/pythonx/elixir_helpers.py
from elixir_helpers import (
    module_name
)


def key_closing(opening: str) -> str:
    """
    Determine key closing character.
    """
    return "," if opening == ":" else ":"

def module_parts(path: str) -> list[str]:
    """
    Return Elixir module and file name from a string path.
    """
    return module_name(path).rsplit(".", 1)
