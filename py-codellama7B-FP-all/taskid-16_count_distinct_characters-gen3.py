def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    characters_set = set()

    for character in string:
        if character not in characters_set:
            characters_set.add(character)

    return len(characters_set)
