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

    # =================
    # Note:
    # - 1. If the input is 1, the answer is "1".
    # - 2. If the input is 0, the answer is "0".
    # - 3. If the input is greater than 1, then the output is:
    #       binary_sum of digits of input.
    # =================
    return str(bin(N).split("b")[1])
