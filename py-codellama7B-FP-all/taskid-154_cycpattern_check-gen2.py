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

    if len(a) < len(b):
        a, b = b, a
    if len(b) == 0:
        return True

    i = 0
    while True:
        i = a.find(b, i)
        if i == -1:
            return False
        if a[i+len(b):i+2*len(b)] == b:
            return True
        i += 1
