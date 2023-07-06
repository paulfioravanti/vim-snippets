"""
Elixir-related Ultisnips snippet helper functions.
NOTE: Changes to this file require restarting Vim!
"""
import re


_DASHES_AND_UNDERSCORES = re.compile(r"[-_]")
_FILE_EXTENSIONS = re.compile(r"\.(?:html\.(?:h|l)?eex|ex)$")
_NON_MODULE_DIRNAMES = [
    "controllers",
    "lib",
    "live",
    "views"
]

def module_name(path):
    """
    Return a full Elixir module name from a file path.
    """
    return ".".join(_module_parts(path))

def root_module_name(path):
    """
    Return name for a root Elixir module from a file path.
    """
    return _module_parts(path)[0]

def to_module_name(string):
    """
    Convert string into an Elixir module name
    """
    string = re.sub(_FILE_EXTENSIONS, "", string)
    string = re.sub(_DASHES_AND_UNDERSCORES, " ", string)
    return string.title().replace(" ", "")

def _module_parts(path):
    path_parts = path.split("/")
    for dirname in _NON_MODULE_DIRNAMES:
        if dirname in path_parts:
            path_parts.remove(dirname)
    return list(map(to_module_name, path_parts))
