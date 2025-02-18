def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """

    c0 = [0] * 26
    c1 = [0] * 26
    for i, c in enumerate(s0):
        c0[ord(c) - ord('a')] += 1
    for i, c in enumerate(s1):
        c1[ord(c) - ord('a')] += 1
    return all(i == j for i, j in zip(c0, c1))
