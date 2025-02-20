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


    def cyclic_rotate(word: str) -> list:
        return [word[i:] + word[:i] for i in range(len(word))]

    cyc_word = cyclic_rotate(b)
    cyc_word.append(b)
    return any(c in a for c in cyc_word)
