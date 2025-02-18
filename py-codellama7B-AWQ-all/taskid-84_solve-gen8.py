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

    # --- Test cases ---
    assert solve(1000) == '1'
    assert solve(150) == '110'
    assert solve(147) == '1100'

    # --- Solve ---
    return bin(N)[2:]
