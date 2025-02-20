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

    binary_list = []
    if N == 0:
        return "0"
    
    while N != 0:
        binary_list.append(str(N % 2))
        N = int(N/2)
    
    return "".join(binary_list[::-1])
