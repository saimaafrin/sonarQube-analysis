def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing('<')
    False
    >>> correct_bracketing('<>')
    True
    >>> correct_bracketing('<<><>>')
    True
    >>> correct_bracketing('><<>')
    False
    """

    # The opening bracket is "<" and the closing bracket is ">"
    opening_bracket = "<"
    closing_bracket = ">"

    opening_brackets = []  # list of all the opening brackets

    # Iterate through the brackets and create a list of opening brackets
    for bracket in brackets:
        if bracket == opening_bracket:
            opening_brackets.append(bracket)

    # Checks if every opening bracket has a corresponding closing bracket
    for opening_bracket in opening_brackets:
        if opening_bracket not in brackets:
            return False

    return True
