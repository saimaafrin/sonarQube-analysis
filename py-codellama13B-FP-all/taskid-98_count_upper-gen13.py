def count_upper(s: str) -> int:
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    >>> count_upper('aBCdEf')
    1
    >>> count_upper('abcdefg')
    0
    >>> count_upper('dBBE')
    0
    """

    # raise NotImplementedError
    result = 0
    length = len(s)
    for i in range(0, length, 2):
        if s[i].isupper():
            result += 1
    return result
