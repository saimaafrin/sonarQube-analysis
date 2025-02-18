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

    # raise NotImplementedError("TODO")
    counter = 0
    for i in range(len(s)):
        if (i % 2 == 0) and (s[i].isupper()):
            counter += 1
    return counter
