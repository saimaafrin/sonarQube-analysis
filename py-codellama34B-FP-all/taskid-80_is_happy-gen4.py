def is_happy(s: str) -> bool:
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    >>> is_happy('a')
    False
    >>> is_happy('aa')
    False
    >>> is_happy('abcd')
    True
    >>> is_happy('aabb')
    False
    >>> is_happy('adb')
    True
    >>> is_happy('xyy')
    False
    """

    # The length of the string is less than 3, it cannot be happy
    if len(s) < 3:
        return False

    # Create a list of 3 letter sequences in the string
    seqs = [s[i : i + 3] for i in range(len(s) - 2)]

    # Check if any of the sequences are the same
    for i in range(len(seqs) - 1):
        if seqs[i] == seqs[i + 1]:
            return False

    return True
