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
    for i, ch in enumerate(s):
        if ch.isupper() and (i + 1) % 2 == 0:
            cnt += 1
    return cnt
