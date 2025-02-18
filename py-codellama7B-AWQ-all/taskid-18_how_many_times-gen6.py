def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    if string == '':
        return 0
    if substring == '':
        return 1

    sub_len = len(substring)
    string_len = len(string)

    max_index = string_len - sub_len
    count = 0

    for index in range(max_index + 1):
        if string[index:index + sub_len] == substring:
            count += 1

    return count
