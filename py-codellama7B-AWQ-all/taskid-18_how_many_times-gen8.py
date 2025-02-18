def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    substring_len = len(substring)
    if substring_len == 0:
        return 0

    return sum(1 for i in range(len(string) - substring_len + 1) if string[i:i+substring_len] == substring)
