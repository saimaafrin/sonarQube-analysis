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

    "*** YOUR CODE HERE ***"
    # if brackets is empty, return True
    if not brackets:
        return True

    # if brackets start with '>', return False
    if brackets[0] == '>':
        return False

    # if brackets start with '<', remove the first character
    # call the function on the remaining string
    if brackets[0] == '<':
        return correct_bracketing(brackets[1:])

    # if brackets start with '><' or '>>', return False
    if brackets[:2] == '><' or brackets[:2] == '>>':
        return False

    # if brackets start with '<<', remove the first two characters
    # call the function on the remaining string
    if brackets[:2] == '<<':
        return correct_bracketing(brackets[2:])

    # if brackets start with '><>', remove the first two characters
    # call the function on the remaining string
    if brackets[:2] == '><':
        return correct_bracketing(brackets[2:])
