def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    i = 0
    while string[i] != '':
        i += 1
    return i
