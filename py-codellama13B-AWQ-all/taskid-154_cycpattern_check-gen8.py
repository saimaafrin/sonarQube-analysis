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

    # if b in a:
    #     return True
    # else:
    #     return False

    # for i in range(1, len(b)):
    #     if b[i:] + b[:i] in a:
    #         return True
    # return False

    # Alternative:
    if b not in a:
        return False
    else:
        return True

    # return (b in a) or (b[1:] in a) or (b[2:] in a) or (b[3:] in a)
