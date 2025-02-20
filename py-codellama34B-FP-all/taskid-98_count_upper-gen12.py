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
    even_upper = 0

    for i in range(len(s)):
        if s[i] in vowels:
            if i % 2 == 0:
                even_upper += 1

    return even_upper
