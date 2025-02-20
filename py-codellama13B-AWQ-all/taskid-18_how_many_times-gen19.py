def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    if len(substring) == 0:
        return len(string)

    count = 0
    i = 0
    while i < len(string):
        if string[i:i+len(substring)] == substring:
            count += 1
            i += len(substring)
        else:
            i += 1
    return count
