def cycpattern_check(a: str, b: str) -> bool:
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    >>> cycpattern_check('abcd', 'abd')
    False
    >>> cycpattern_check('hello', 'ell')
    True
    >>> cycpattern_check('whassup', 'psus')
    False
    >>> cycpattern_check('abab', 'baa')
    True
    >>> cycpattern_check('efef', 'eeff')
    False
    >>> cycpattern_check('himenss', 'simen')
    True

    """

    # If the second word is a substring of the first word
    if b in a:
        return True
    # If the second word is the same as the first word
    elif a == b:
        return True
    # If the length of the second word is smaller than the first word
    elif len(a) > len(b):
        # Loop through the length of the second word
        for i in range(len(b)):
            # Get the substring from the second word starting from index 0 to the length of the second word
            substr = b[0:i]
            # Check if the substring is a substring in the first word
            if substr in a:
                # If it is, check if the substring is the same as the second word
                if substr == b:
                    # If it is, return False since it is a substring in the first word but not a rotation of it
                    return False
                # If it is not, return True since it is a rotation
                else:
                    return True
        # If the second word is not a substring in the first word
        return False
    # If the length of the second word is bigger than the first word
    else:
        # If the second word is a substring in the first word
        if b in a:
            # If the second word is the same as the first word
            if b == a:
                # If it is, return False since it is a substring in the first word but not a rotation of it
                return False
            # If it is not, return True since it is a rotation
            else:
                return True
        # If the second word is not a substring in the first word
        return False
