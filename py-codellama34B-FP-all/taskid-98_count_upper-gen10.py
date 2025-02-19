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
    
    even_indices = s[1::2]
    return sum(c.isupper() for c in even_indices)
