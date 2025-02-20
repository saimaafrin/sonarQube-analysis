def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a) != len(b):
        raise ValueError("Strings must be of equal length")
    if a.isdigit() and b.isdigit():
        # If string contains only digits, use int()
        return bin(int(a, 2) ^ int(b, 2))[2:].rjust(len(a), '0')
    else:
        # If string contains non-digits, use zip()
        return ''.join(str(int(a_i != b_i)) for a_i, b_i in zip(a, b))
