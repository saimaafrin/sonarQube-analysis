def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    if string is None:
        return 0
    else:
        distinct_chars = set()
        for char in string:
            distinct_chars.add(char.lower())

        return len(distinct_chars)
