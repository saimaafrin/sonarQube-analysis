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

    if s == '':
        return False
    if len(s) < 3:
        return False
    if s[0] == s[1] and s[1] == s[2]:
        return False
    if s[1] == s[2] and s[2] == s[3]:
        return False
    if s[2] == s[3] and s[3] == s[4]:
        return False
    return True
