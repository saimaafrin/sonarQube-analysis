def correct_bracketing(brackets: str) -> bool:
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing('(')
    False
    >>> correct_bracketing('()')
    True
    >>> correct_bracketing('(()())')
    True
    >>> correct_bracketing(')(()')
    False
    """


    # Base case
    if len(brackets) == 0:
        return True

    if brackets[0] == "(":
        return correct_bracketing(brackets[1:])
    else:
        # Check if the first character is a closing bracket
        if brackets[0] == ")":
            return False
        # Check if the first opening bracket has a corresponding closing bracket
        if not has_matching_closing_bracket(brackets):
            return False
        else:
            # Check if the rest of the string is correctly bracketed
            return correct_bracketing(brackets[1:])
