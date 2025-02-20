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
    binary = str(bin(N)[2:])

    # initialize sum variable
    sum = 0

    # loop through each element
    for b in binary:
        sum += int(b)

    # return the result
    return str(sum)
