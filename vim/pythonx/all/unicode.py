"""
Companion python file for `unicode.snippets` file.
NOTE: Changes to this file require restarting Vim!
"""

def number_to_die_face(number: str) -> str:
    """
    Return appropriate die face character given a number.
    """
    die_face: str

    match int(number):
        case 1:
            die_face = "⚀"
        case 2:
            die_face = "⚁"
        case 3:
            die_face = "⚂"
        case 4:
            die_face = "⚃"
        case 5:
            die_face = "⚄"
        case 6:
            die_face = "⚅"
        case _:
            die_face = "□"

    return die_face
