def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    return ''.join('1' if a[i] == '1' and b[i] == '1' else '0' for i in range(len(a)))
