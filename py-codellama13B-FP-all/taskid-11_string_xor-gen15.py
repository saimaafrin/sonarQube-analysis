def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    assert len(a) == len(b), 'a and b must be of same length'
    assert set(a) == set(b) == {'1', '0'}, 'a and b must consist only of 1s and 0s'

    return ''.join(map(lambda x, y: str(int(x) ^ int(y)), a, b))
