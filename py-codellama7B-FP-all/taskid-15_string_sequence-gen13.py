def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    string = ""
    for i in range(n+1):
        if i == 0:
            string += str(i)
        else:
            string += " " + str(i)
    return string
