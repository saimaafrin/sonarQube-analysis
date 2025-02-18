def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    # If the substring is empty, return 0
    if not substring:
        return 0
    # If the original string is empty, return 0
    if not string:
        return 0
    # Count the number of occurrences of the substring in the original string
    return string.count(substring)
