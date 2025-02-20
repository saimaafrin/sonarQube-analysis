def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    if not string:
        return 0

    characters = {}
    for character in string.lower():
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1

    return len(characters)
