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

    # Write your code here
    binary = "1"
    while N > 1:
        N = N >> 1
        binary += "1"
    return binary
