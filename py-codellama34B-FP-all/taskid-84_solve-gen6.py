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

    # 1. Convert number to binary
    # 2. Sum all the digits
    # 3. Return the sum of the digits
    # 4. Convert the sum to binary
    return bin(sum(map(int, bin(N)[2:])))[2:]
