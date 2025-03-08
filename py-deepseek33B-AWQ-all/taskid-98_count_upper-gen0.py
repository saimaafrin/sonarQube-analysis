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

    count = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] in 'AEIOU':
            count += 1
    return count
