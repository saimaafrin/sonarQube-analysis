def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    count = 0
    while True:
        start_pos = string.find(substring)
        if start_pos == -1:
            break
        count += 1
        string = string[start_pos + 1 :]
    return count
