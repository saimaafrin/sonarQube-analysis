def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    result = ''
    for c1, c2 in zip(a, b):
        result += str(int(c1) ^ int(c2))

    return result
