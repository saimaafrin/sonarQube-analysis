def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    assert isinstance(a, str) and isinstance(b, str)
    result = ""
    for char_a, char_b in zip(a, b):
        result += str(int(char_a) ^ int(char_b))
    return result
