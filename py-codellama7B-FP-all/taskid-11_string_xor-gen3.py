def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """


    # Convert to int
    a = int(a, 2)
    b = int(b, 2)

    # Perform XOR
    result = a ^ b

    # Convert back to string
    result_bin = bin(result)[2:]
    result_bin = result_bin.zfill(len(a))

    return result_bin
