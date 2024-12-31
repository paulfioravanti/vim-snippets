"""
Companion python file for `python/classes.snippets` file.
"""

# Cannot type hint a `snip`.
# pylint: disable=duplicate-code
def initialize_args(snip, init_tabstop_index, starting_tabstop_index):
    """
    Initialise arguments in a Python class
    """
    if (
        not snip.tabstop == 0 or
        not (args_tabstop := snip.tabstops[init_tabstop_index])
    ):
        return

    # Strip out all the surrounding tabstop characters
    args_list = (
        args_tabstop
        .current_text
        .removeprefix("def __init__(self")
        .removesuffix("):")
        .split(",")
    )

    args = [string.strip() for string in args_list if string]
    tabstop_indexes = range(
        starting_tabstop_index,
        starting_tabstop_index + len(args)
    )

    output = ""
    for arg, index in zip(args, tabstop_indexes, strict=True):
        output += f"\n    self.{arg} = ${{{index}:{arg}}}"

    snip.expand_anon(output)
