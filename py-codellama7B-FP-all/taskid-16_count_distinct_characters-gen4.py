def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    chars = {}
    for char in string:
        if char.lower() not in chars:
            chars[char.lower()] = char
    return len(chars)
