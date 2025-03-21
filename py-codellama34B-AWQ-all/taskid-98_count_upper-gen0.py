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

    vowels = 'aeiou'
    vowels = [c.upper() for c in vowels]
    return sum(s[i].upper() in vowels for i in range(0, len(s), 2))
