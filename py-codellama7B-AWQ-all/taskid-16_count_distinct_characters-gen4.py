def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """


    count = 0
    seen = set()

    for char in string.upper():
        if char not in seen:
            seen.add(char)
            count += 1
    return count
