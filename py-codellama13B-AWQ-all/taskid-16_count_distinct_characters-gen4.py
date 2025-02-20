def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """


    # O(n) solution
    # return len(set(string.lower()))

    # O(n) solution
    # return len(set(c for c in string.lower()))

    # O(n) solution
    # return len(set(c.lower() for c in string))

    # O(n) solution
    return len({c.lower() for c in string})
