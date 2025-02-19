def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    index = 0
    count = 0
    while index < len(string):
        if substring in string[index:]:
            count += 1
            index = string.index(substring, index) + 1
        else:
            index = len(string) + 1
    return count
