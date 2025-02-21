def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    res = ""
    for i in range(len(a)):
        res += str(int(a[i]) ^ int(b[i]))
    return res
