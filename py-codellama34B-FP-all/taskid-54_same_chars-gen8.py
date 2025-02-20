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

    # TODO: Implement this function to return True if s0 and s1 contain
    # the same characters, False otherwise.
    # HINT: s0 and s1 can be sorted with the sorted() function.
    # HINT: Use the == operator to compare strings.
    # HINT: This can be done in one line.
    return sorted(s0) == sorted(s1)
