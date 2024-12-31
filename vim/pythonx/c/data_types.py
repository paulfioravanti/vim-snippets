"""
Companion python file for `c/data_types.snippets` file.
"""

def type_var_placeholder(typedef_tabstop: str) -> str:
    """
    Determine placeholder based on tabstop value.
    """
    return "TypeName" if typedef_tabstop else "variable_name"
