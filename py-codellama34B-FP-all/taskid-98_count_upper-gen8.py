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

    even_indices = s[0::2]
    uppercase_vowels = {c for c in even_indices if c in 'AEIOU'}
    return len(uppercase_vowels)
