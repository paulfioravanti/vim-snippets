"""
Companion python file for `javascript/function.snippets` file.
"""

# Cannot type hint a `snip`.
# pylint: disable=duplicate-code
def initialize_args(snip, init_tabstop_index, starting_tabstop_index):
    """
    Initialise arguments for a Javascript class.
    """
    if (
        not snip.tabstop == starting_tabstop_index or
        not (args_tabstop := snip.tabstops[init_tabstop_index])
    ):
        return

    # Strip out all the surrounding tabstop characters
    args_list = (
        args_tabstop
        .current_text
        .removeprefix("  constructor(")
        .removesuffix(") {\n  }")
        .split(",")
    )

    args = [string.strip() for string in args_list if string]
    tabstop_indexes = range(
        starting_tabstop_index,
        starting_tabstop_index + len(args)
    )

    output = ""
    for arg, index in zip(args, tabstop_indexes, strict=True):
        output += f"\n  this.{arg} = ${{{index}:{arg}}};"

    snip.expand_anon(output)
