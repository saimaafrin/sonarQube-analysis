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

    brackets = list(brackets)
    if brackets.count('(') != brackets.count(')'):
        return False

    for i, bracket in enumerate(brackets):
        if bracket == ')':
            if i == 0 or brackets[i - 1] != '(':
                return False
            brackets.pop(i)
            brackets.pop(i - 1)
            return correct_bracketing("".join(brackets))

    return True
