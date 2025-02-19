def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    counter = 0
    start_idx = 0
    end_idx = len(substring)

    while end_idx <= len(string):
        if string[start_idx:end_idx] == substring:
            counter += 1
        start_idx += 1
        end_idx += 1

    return counter
