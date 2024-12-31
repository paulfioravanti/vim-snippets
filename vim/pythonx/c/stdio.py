"""
Companion python file for `c/stdio.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

# Cannot type hint a `snip`.
# pylint: disable-next=line-too-long
# Adapted from https://github.com/honza/vim-snippets/blob/a8dc763b3f534ec1a0c0ae5082689c10dcaf9d5f/UltiSnips/c.snippets#L8-L24
# pylint: disable=duplicate-code
def printf_expand_args(
    snip,
    format_tabstop_index,
    placeholder_args_index,
    next_tabstop_index
):
    """
    This will look how many placeholders printf has and adds the separated
    commas at the end.
    """
    if not snip.tabstop == placeholder_args_index:
        return

    # now add so many "," as much as the amount of placeholders
    amount_placeholders = (
        snip.tabstops[format_tabstop_index].current_text.count("%")
    )
    final_tabstop_index = next_tabstop_index + amount_placeholders
    output = ""

    # Add the amount of tabstops
    for placeholder_index in range(next_tabstop_index, final_tabstop_index):
        output.join(f", ${placeholder_index}")

    # convert them into tabstops
    snip.expand_anon(output)
