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

    
    binary_N = bin(N)
    binary_N = binary_N[2:]
    sum = 0
    for digit in binary_N:
        sum += int(digit)
    return bin(sum)[2:]
