def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    # Fill in your code here
    #return '111'
    #return a
    #return b
    #return a[1]
    #return b[1]
    #return a[0]
    #return b[0]
    #return a[0:1] + b[0:1]
    #return a[0:2] + b[0:2]
    #return a[1:] + b[1:]
    #return a[2:] + b[2:]
    #return a[1:2] + b[1:2]
    #return a[1:3] + b[1:3]
    #return a[2:3] + b[2:3]
    return ''.join(map(lambda x, y: str(int(x) ^ int(y)), a, b))
