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

    bracket_pairs = {")": "("}
    opening = []
    for char in brackets:
        if char in bracket_pairs:
            if len(opening) == 0 or bracket_pairs[char] != opening.pop():
                return False
        else:
            opening.append(char)
    return len(opening) == 0
