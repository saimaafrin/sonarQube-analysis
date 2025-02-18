def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    # Count the number of times each character appears
    counts = {char: string.lower().count(char) for char in string}
    # Keep only the characters that appeared at least once
    return len(set(char for char, _ in counts.items() if counts[char] > 0))
