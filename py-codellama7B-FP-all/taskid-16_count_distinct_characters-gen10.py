def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # lowercase everything
    string = string.lower()
    # convert to set to get rid of duplicates
    unique_characters = set(string)
    # convert back to list for return
    return len(list(unique_characters))
