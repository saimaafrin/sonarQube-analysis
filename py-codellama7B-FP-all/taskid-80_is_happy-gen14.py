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

    # If the string is at least 3 characters long
    if len(s) >= 3:
        # Then check if the first three letters are different
        if s[0] != s[1] and s[0] != s[2] and s[1] != s[2]:
            # If they are different then check the remaining letters
            for i in range(2, len(s)):
                # If three consecutive letters are not different
                # then return false
                if s[i] == s[i + 1] and s[i] == s[i + 2]:
                    return False
            # If we reached here then all three consecutive letters
            # are different
            # So return true
            return True
    # If the string is less than 3 characters long
    # then it cannot be happy
    return False
