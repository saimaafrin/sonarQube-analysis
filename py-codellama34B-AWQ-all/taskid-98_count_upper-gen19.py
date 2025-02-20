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

    vowels = 'AEIOU'
    n = 0
    for i, c in enumerate(s):
        if c in vowels and i % 2 == 0:
            n += 1
    return n
