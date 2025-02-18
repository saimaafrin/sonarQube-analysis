def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    return len([i for i, j in enumerate(string) if i != 0 and j == substring[0] and string[i - 1] == substring[len(substring) - 1]])
