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
    binary_list = list()
    while N > 0:
        binary_list.append(str(N % 2))
        N //= 2
    binary_list.reverse()
    binary_str = ''.join(binary_list)
    
    # convert to int and back to binary
    N = int(binary_str, base=2)
    binary_list = list()
    while N > 0:
        binary_list.append(str(N % 2))
        N //= 2
    binary_list.reverse()
    binary_str = ''.join(binary_list)
    
    return binary_str
