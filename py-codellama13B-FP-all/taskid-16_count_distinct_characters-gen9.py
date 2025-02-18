def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # Using dictionary to keep track of the characters
    char_dict = {}
    for char in string:
        char_dict[char] = True
    return len(char_dict.keys())
