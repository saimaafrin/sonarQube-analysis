def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if not a or not b:
        return ''
    result = []
    for c1, c2 in zip(a, b):
        if c1 == c12 == '1':
            result.append('0')
        elif c1 == '1' and c2 == '0':
            result.append('1')
        elif c2 == '1' and c1 == '0':
            result.append('1')
        else:
            result.append('0')
    return ''.join(result)
