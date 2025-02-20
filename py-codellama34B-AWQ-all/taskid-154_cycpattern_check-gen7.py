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

    def rotate(word):
        return word[1:] + word[0]

    a = a.lower()
    b = b.lower()
    b = b.replace(b[0], '')
    while len(b) > 0:
        if b in a:
            return True
        b = rotate(b)
    return False
