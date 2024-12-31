"""
Companion python file for `c/stdio.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

# ~/.vim/pythonx/global_helpers.py
from global_helpers import (
    snake_to_camel
)


# Cannot type hint a `snip`.
def controller_class_resource_name(snip):
    """
    Provide default name for a resource in a Rails controller class.
    """
    return snake_to_camel(controller_file_resource_name(snip))

# Cannot type hint a `snip`.
def controller_file_resource_name(snip):
    """
    Provide default name for a resource from a Rails controller file.
    """
    return snip.basename.replace("_controller", "")

def controller_model_default(controller_variable: str) -> str:
    """
    Provide default name for a model in a Rails controller file.
    """
    return snake_to_camel(controller_variable)

# Cannot type hint a `snip`.
def controller_singular_variable(snip):
    """
    Provide default name for a singular variable in a Rails controller file.
    """
    controller_resource_name = controller_file_resource_name(snip)
    if controller_resource_name.endswith("s"):
        return controller_resource_name[:-1]

    # Plural does not end in "s", and we do not have a plural/singular
    # dictionary to work with, so just return the plural name and correct it
    # within the snippet inline.
    return controller_resource_name

def params_id(controller_name: str, variable: str, model_name: str) -> str:
    """
    Provide default name for the params id in a Rails controller file.
    """
    if model_name == controller_name.rstrip("s"):
        return "id"

    return variable + "_id"
