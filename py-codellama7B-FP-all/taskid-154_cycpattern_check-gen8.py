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
    if len(a) < len(b):
        return False
    a_list = list(a)
    b_list = list(b)
    for i in range(len(b_list)):
        a_list.append(a_list.pop(0))
        a_rotated = ''.join(a_list)
        if b_list == a_list or b_list == a_rotated:
            return True
    return False
