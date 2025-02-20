def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a) != len(b):
        raise ValueError('Length of a and b do not match')
    res = []
    for x, y in zip(a, b):
        res.append('1' if x == '0' and y == '1' or x == '1' and y == '0' else '0')
    return ''.join(res)
