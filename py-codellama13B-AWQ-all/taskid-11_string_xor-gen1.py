def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """


    # If one or both input strings are empty, return empty string
    if a == '' or b == '':
        return ''

    # The two inputs are of equal length
    # The resulting string has length len(a)
    out = ''
    for i in range(len(a)):
        # if i'th char in a is 0, the XOR is 0 iff i'th char in b is also 0
        # Otherwise the XOR is 1
        if a[i] == '0':
            out += b[i]
        else:
            out += '1' if b[i] == '0' else '0'

    return out
