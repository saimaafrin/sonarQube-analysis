def solve(N: int) -> str:
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
    >>> solve(1000)
    '1'
    >>> solve(150)
    '110'
    >>> solve(147)
    '1100'
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """

    # convert to binary
    binary_str = bin(N)
    # remove the '0b' in the left
    binary_str = binary_str[2:]
    # sum the digits
    return str(sum([int(i) for i in binary_str]))
