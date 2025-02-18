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

    return len(
        [c for c in s if c.isupper() and c.lower() in 'aeiou' and c.index(c.lower()) % 2 == 0]
    )
