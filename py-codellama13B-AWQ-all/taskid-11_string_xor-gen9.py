def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """


    if len(a) != len(b):
        raise ValueError('Both inputs must be of the same length.')

    result = ''
    for c1, c2 in zip(a, b):
        if c1 == '1' and c2 == '1':
            result += '0'
        elif c1 == '0' and c2 == '0':
            result += '0'
        else:
            result += '1'

    return result
