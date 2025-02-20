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

    c = 0
    for i, ch in enumerate(s):
        if i % 2 == 1:
            continue
        if ch.isupper():
            c += 1
    return c
