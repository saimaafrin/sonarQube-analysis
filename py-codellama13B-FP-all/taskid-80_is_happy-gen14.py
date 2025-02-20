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

    # The length of string must be greater than or equal to 3
    if len(s) < 3:
        return False

    # Check if the first 3 letters are distinct
    if s[:3] == s[1:4] or s[:3] == s[2:5]:
        return False

    # Check if the string has 3 consecutive letters that are distinct
    for i in range(len(s) - 3):
        if s[i : i + 3] == s[i + 1 : i + 4] or s[i : i + 3] == s[i + 2 : i + 5]:
            return False

    # All good!
    return True
