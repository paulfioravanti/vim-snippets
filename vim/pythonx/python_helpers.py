# ~/.vim/pythonx/global_helpers.py
from global_helpers import (
    snake_to_camel
)

def class_name(snip):
    return snake_to_camel(snip.basename)
