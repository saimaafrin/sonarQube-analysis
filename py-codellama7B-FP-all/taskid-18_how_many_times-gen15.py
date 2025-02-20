def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    n = 0
    i = 0
    while i < len(string):
        j = i
        while j < len(string) and string[j] == substring[0]:
            if string[j:j + len(substring)] == substring:
                n += 1
            j += 1
        i += 1
    return n
