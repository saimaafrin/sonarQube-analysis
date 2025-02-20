def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    assert all(i in '10' for i in a + b)
    return ''.join(str(int(i) ^ int(j)) for i, j in zip(a, b))
