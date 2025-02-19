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

    if N == 0:
        return "0"
    bin_str = ''
    while N > 0:
        if N % 2 == 1:
            bin_str = '1' + bin_str
        else:
            bin_str = '0' + bin_str
        N //= 2
    return bin_str
