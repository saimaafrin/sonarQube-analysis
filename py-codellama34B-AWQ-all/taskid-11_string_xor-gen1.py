def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    assert len(a) == len(b), "String a and b must be of equal length"
    assert set(a).issubset({'0', '1'}), "String a can only contain 0s and 1s"
    assert set(b).issubset({'0', '1'}), "String b can only contain 0s and 1s"
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
