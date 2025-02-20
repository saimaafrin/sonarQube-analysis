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

    # We could get fancy here and make use of regular expressions
    # But that would be overkill for this question
    
    # Count the number of uppercase vowels in even indices
    count = 0
    for i in range(0, len(s), 2):
        # Only count if we're on an even index, otherwise we
        # would count the first vowel twice
        if s[i].isupper():
            count += 1
    
    return count
