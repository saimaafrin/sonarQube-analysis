def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # The idea is simple, we can just convert the string to lowercase, and then count
    # distinct characters (which are also lowercase).
    #
    # A better idea is to actually use a `set`, which is much faster, because we
    # can look up each character in it and it will take O(1) time.

    return len(set(string.lower()))
