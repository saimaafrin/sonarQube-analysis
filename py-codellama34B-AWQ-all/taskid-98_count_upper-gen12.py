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

    vowels = ('a', 'e', 'i', 'o', 'u')
    return sum(s[i].isupper() and s[i] in vowels for i in range(0, len(s), 2))
