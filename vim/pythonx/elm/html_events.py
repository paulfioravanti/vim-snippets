"""
Companion python file for `elm/html_events.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

def words_to_function(words: str) -> str:
    """
    Convert words to a valid Elm function name.
    """
    head, *tail = words.split(" ")
    tail = [word.capitalize() for word in tail]
    return "".join([head, *tail])
