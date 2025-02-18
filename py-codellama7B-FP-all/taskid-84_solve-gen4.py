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

    
    # check N is within constraints
    assert 0 <= N <= 10000, 'Error: N is out of constraints!'
    
    # declare a new variable to store the result
    result = 0
    
    # while N > 0
    while N > 0:
        # calculate the digit of N
        digit = N % 2
        
        # calculate the total sum
        result += digit
        
        # calculate N / 2
        N //= 2
    
    # return the total sum
    return str(result)
