def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    assert len(a) == len(b), 'Input string length not same!'

    # initialize the empty string
    result = ''

    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))

    return result
