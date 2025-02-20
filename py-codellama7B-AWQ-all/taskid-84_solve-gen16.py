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

    assert isinstance(N, int), "Input should be a positive integer."
    assert N <= 10000, "Input should be a positive integer no larger than 10000."
    
    # convert the integer to binary
    return bin(N)[2:]
