def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    # Convert both inputs to integer
    a_int = int(a, 2)
    b_int = int(b, 2)

    # XOR them and convert result to binary string
    res_int = a_int ^ b_int
    res_bin = bin(res_int)[2:]
    return res_bin.zfill(len(a))
