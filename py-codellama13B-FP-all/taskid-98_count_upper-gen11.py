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


    upper_count = 0
    for idx in range(len(s)):
        if idx % 2 == 0 and s[idx].isupper():
            upper_count += 1

    return upper_count
