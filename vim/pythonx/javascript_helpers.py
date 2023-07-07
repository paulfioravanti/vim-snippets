"""
JavaScript-related Ultisnips snippet helper functions.
Based off https://github.com/honza/vim-snippets/blob/master/pythonx/javascript_snippets.py
NOTE: Changes to this file require restarting Vim!
"""
import re
from UltiSnips import vim_helper


# REF: https://stackoverflow.com/a/3469155/567863
_NON_NEWLINE_WHITESPACE = "[^\S\r\n]"

def class_attribute_name():
    """
    Determines the class attribute name of a tag based on the file type.
    This handling is needed specifically for React.
    """
    # NOTE: snip.ft not available during pre_expand/post_jump, which is when
    # this function is used (html.snippets).
    # See SnippetUtilForAction class in Ultisnips codebase to show that it only
    # responds to `expand_anon`:
    # https://github.com/SirVer/ultisnips/blob/master/pythonx/UltiSnips/text_objects/python_code.py
    return "className" if vim_helper.eval("&filetype") == "javascript" else "class"

def maybe_semi(snip):
    # NOTE: This guard is needed to prevent recursion bugs when starting a
    # snippet and then running undo before the snippet has finished.
    # See: https://github.com/SirVer/ultisnips/issues/375#issuecomment-55115227
    if not snip.c:
        option = _get_config_option(snip, "semi", "always")
        snip.rv = ";" if option == "always" else ""

def maybe_spaces(tabstop):
    if not tabstop:
        return ""

    # Match spaces on one-line functions only, not multiline.
    trailing_spaces = re.match(
        rf"^{tabstop[0]}({_NON_NEWLINE_WHITESPACE}+)",
        tabstop
    )

    return trailing_spaces.group(1) if trailing_spaces else ""

def _get_config_option(snip, option, default=None):
    """
    Gets a config option from ~/.vim/settings/ultisnips.vim
    """
    return snip.opt('g:ultisnips_javascript["{}"]'.format(option), default)
