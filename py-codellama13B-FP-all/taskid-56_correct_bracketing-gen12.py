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


    # your code here
    if len(brackets) % 2 != 0:
        return False
    s = Stack()
    for b in brackets:
        if b == "<":
            s.push(b)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()
    if s.is_empty():
        return True
    else:
        return False
