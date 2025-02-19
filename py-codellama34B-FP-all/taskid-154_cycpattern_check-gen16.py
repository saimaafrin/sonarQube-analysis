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

    b_len = len(b)
    if b_len > len(a):
        return False
    for i in range(len(a)):
        if a[i:i + b_len] == b:
            return True
        if i + b_len < len(a) and a[i + b_len] == b[0]:
            continue
        else:
            break
    return False
