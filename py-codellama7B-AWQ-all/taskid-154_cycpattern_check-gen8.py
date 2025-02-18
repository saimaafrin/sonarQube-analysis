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

    if a == b:
        return True
    elif a == "":
        return False
    else:
        for i in range(len(b)):
            if b[i] in a:
                if b[i:] in a:
                    return True
                else:
                    return False
            else:
                return False
