def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    assert set(a).issubset({'0', '1'})
    assert set(b).issubset({'0', '1'})
    assert len(a) == len(b)

    result = ""
    for c, d in zip(a, b):
        if c == d:
            result += '0'
        else:
            result += '1'
    return result
