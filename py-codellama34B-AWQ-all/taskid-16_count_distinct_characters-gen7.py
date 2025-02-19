def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """


    # string: the string to search
    # return: the number of distinct characters in the string

    seen = set()  # create an empty set
    for c in string:
        if c.lower() not in seen:
            seen.add(c.lower())
    return len(seen)
