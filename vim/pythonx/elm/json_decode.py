"""
Companion python file for `elm/json_decode.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

from typing import Match


def decode_primitive_name(string: str) -> str:
    """
    Return primative name for a decoder.
    """
    return "int" if string == "integer" else string

# Cannot type hint a `snip`.
def build_map_function(snip, number_of_decoders):
    """
    Build a Json.Decode.map function within a snip.
    """

    output = (
        f"${{1:Json.}}Decode.map{number_of_decoders} ${{2:valueFunction}}"
    )
    tabstop_indexes = range(3, 3 + number_of_decoders)

    for index in tabstop_indexes:
        output += f"\n    (${{{index}:decoder}})"

    snip.expand_anon(output)

def decoder_default_text(match: Match, json_top_level_module: str) -> str:
    """
    Return default text for a named decoder.
    """
    match match.group(1).strip():
        case "bool":
            decoder = "Decode.bool"
        case "float":
            decoder = "Decode.float"
        case "int":
            decoder = "Decode.int"
        case "integer":
            decoder = "Decode.int"
        case "string":
            decoder = "Decode.string"
        case _:
            decoder = "decoder"

    if decoder == "decoder":
        return decoder

    if json_top_level_module:
        decoder = json_top_level_module + decoder

    return decoder
