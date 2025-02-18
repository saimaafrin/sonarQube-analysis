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


    if len(brackets) % 2 == 1:
        return False

    bracket_count = 0

    for i in range(len(brackets)):
        if brackets[i] == "<":
            bracket_count += 1
        elif brackets[i] == ">":
            bracket_count -= 1

        if bracket_count < 0:
            return False

    return bracket_count == 0
