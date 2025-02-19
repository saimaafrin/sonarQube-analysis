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


    def _int_to_binary(n: int) -> str:
        """Convert integer to binary.
        Args:
            n (int): integer
        Return:
            (str): binary
        """
        return bin(n)[2:]

    def _sum_of_digits(s: str) -> str:
        """Sum of digits of a string.
        Args:
            s (str): binary string
        Return:
            (str): sum of digits of a string
        """
        return str(sum(map(int, s)))

    return _sum_of_digits(_int_to_binary(N))
