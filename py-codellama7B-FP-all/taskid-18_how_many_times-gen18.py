def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    start = 0
    count = 0
    while True:
        i = string.find(substring, start)
        if i == -1:
            break
        count += 1
        start = i + 1
    return count
