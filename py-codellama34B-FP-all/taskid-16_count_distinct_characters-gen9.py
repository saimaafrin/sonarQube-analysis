def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    char_map = {}
    string = string.lower()

    for char in string:
        if char in char_map:
            continue

        char_map[char] = True

    return len(char_map)
