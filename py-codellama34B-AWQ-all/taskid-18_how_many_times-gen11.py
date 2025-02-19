def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    if string == '':
        return 0
    else:
        return len([x for x in range(0, len(string) - len(substring) + 1) if string[x:x + len(substring)] == substring])
