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


    def convert_to_binary(n):
        return bin(n)[2:]

    return "".join(map(lambda x: str(x), [sum(int(x) for x in convert_to_binary(N))]))
