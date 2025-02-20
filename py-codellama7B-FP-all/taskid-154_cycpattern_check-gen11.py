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


    # A = 'abcd'
    # B = 'abd'
    a_len = len(a)
    b_len = len(b)
    # A = 'efef'
    # B = 'eeff'
    # b_len = 4
    # b = 'eeff'
    # a_len = 4
    # b_len = len(b)

    if a_len < b_len:
        return False
    else:
        for _ in range(b_len):
            b = b[1:] + b[0]

            if b in a:
                return True
        return False
