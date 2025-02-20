def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a) != len(b):
        raise ValueError(
            f"XOR between two string of different lengths: {len(a)} != {len(b)}"
        )
    result = ""
    for a_char, b_char in zip(a, b):
        if a_char == b_char:
            result += "0"
        else:
            result += "1"
    return result
