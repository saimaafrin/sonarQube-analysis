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

    s0_dict = {}
    for c in s0:
        if c in s0_dict:
            s0_dict[c] += 1
        else:
            s0_dict[c] = 1

    for c in s1:
        if c in s0_dict:
            s0_dict[c] -= 1
        else:
            return False

    return all([c <= 0 for c in s0_dict.values()])
