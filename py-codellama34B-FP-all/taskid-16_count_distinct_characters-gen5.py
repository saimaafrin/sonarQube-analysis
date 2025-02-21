def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    string = string.lower()
    distinct_characters = []
    for character in string:
        if character not in distinct_characters:
            distinct_characters.append(character)
    return len(distinct_characters)
