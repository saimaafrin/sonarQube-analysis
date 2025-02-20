def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    i = 0
    counter = 0
    while True:
        try:
            i = string.index(substring, i)
            counter += 1
        except ValueError:
            break
        i += 1
    return counter
