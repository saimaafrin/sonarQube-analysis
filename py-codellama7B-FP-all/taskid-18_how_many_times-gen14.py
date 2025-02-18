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
    count = 0
    while i < len(string):
        j = 0
        while j < len(substring) and i + j < len(string) and string[i + j] == substring[j]:
            j += 1
        if j == len(substring):
            count += 1
        i += 1
    return count
