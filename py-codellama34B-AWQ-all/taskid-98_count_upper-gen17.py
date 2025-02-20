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

    if not s:
        return 0
    vowels = ('A', 'E', 'I', 'O', 'U')
    return sum(map(s.__contains__, vowels))
