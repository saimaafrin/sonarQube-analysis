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

    cnt = 0
    for i in range(0, len(s), 2):
        c = s[i].upper()
        if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
            cnt += 1
    return cnt
