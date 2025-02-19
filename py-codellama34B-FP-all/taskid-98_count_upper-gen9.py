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

    return len(list(filter(lambda i: i in ['A', 'E', 'I', 'O', 'U'], [s[i] for i in range(0, len(s), 2)])))
