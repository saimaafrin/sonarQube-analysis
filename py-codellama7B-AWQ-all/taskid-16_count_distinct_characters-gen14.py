def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # count_map: Dict[str, int] = {}
    count_map = Counter()
    for c in string:
        count_map[c.lower()] += 1
    return len(count_map)
