"""
JavaScript-related Ultisnips snippet helper functions.
Based off https://github.com/honza/vim-snippets/blob/master/pythonx/javascript_snippets.py
NOTE: Changes to this file require restarting Vim!
"""

def get_config_option(snip, option, default=None):
    """
    Gets a config option from ~/.vim/settings/ultisnips.vim
    """
    return snip.opt('g:ultisnips_javascript["{}"]'.format(option), default)

def maybe_semi(snip):
    option = get_option(snip, "semi", "always")
    return ";" if option == "always" else ""
