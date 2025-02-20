def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """


    if len(a) != len(b):
        raise ValueError(f"{a} and {b} must be of the same length")

    out = ''
    for i in range(len(a)):
        out += str(int(a[i]) ^ int(b[i]))
    return out
