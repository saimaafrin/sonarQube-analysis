def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    assert len(a) == len(b)
    result = ''
    for (char1, char2) in zip(a, b):
        result += str(int(char1) ^ int(char2))
    return result
