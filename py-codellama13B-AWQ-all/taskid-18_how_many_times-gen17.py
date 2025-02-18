def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """


    if substring == '':
        return 0
    if len(substring) > len(string):
        return 0
    count = 0
    index = string.find(substring)
    while index != -1:
        count += 1
        index = string.find(substring, index + 1)
    return count
