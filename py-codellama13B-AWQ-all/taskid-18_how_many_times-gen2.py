def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    result = 0
    substring_length = len(substring)
    for i in range(len(string)):
        if string[i: i + substring_length] == substring:
            result += 1
    return result
