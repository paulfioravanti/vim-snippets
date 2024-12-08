"""
Elixir-related Ultisnips snippet helper functions.
NOTE: Changes to this file require restarting Vim!
"""

import re


_DASHES_AND_UNDERSCORES: re.Pattern = re.compile(r"[-_]")
_FILE_EXTENSIONS: re.Pattern = re.compile(r"\.(?:html\.(?:h|l)?eex|ex)$")
_NON_MODULE_DIRNAMES: list[str] = [
    "controllers",
    "lib",
    "live",
    "views"
]

def module_name(path: str) -> str:
    """
    Return a full Elixir module name from a file path.
    """
    return ".".join(_module_parts(path))

def root_module_name(path: str) -> str:
    """
    Return name for a root Elixir module from a file path.
    """
    return _module_parts(path)[0]

def to_module_name(string: str) -> str:
    """
    Convert string into an Elixir module name
    """
    string = re.sub(_FILE_EXTENSIONS, "", string)
    string = re.sub(_DASHES_AND_UNDERSCORES, " ", string)
    return string.title().replace(" ", "")

def _module_parts(path: str) -> list[str]:
    path_parts = path.split("/")
    for dirname in _NON_MODULE_DIRNAMES:
        if dirname in path_parts:
            path_parts.remove(dirname)
    return [to_module_name(path_part) for path_part in path_parts]
