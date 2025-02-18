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

    # We assume that the input is all lowercase and there are no spaces.
    # If this is not the case, we need to normalize the input to lowercase
    # before we start counting.

    # We also assume that we are counting in an even-indexed manner.
    # If this is not the case, we need to modify the solution accordingly.

    upper = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            upper += 1
    return upper
