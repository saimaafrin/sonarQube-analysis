def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    # Convert inputs to integers.
    a_int = int(a, 2)
    b_int = int(b, 2)

    # XOR
    result_int = a_int ^ b_int

    # Convert result to string.
    result = bin(result_int)[2:]

    return result
