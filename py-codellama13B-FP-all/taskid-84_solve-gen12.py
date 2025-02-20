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

    # Converts N to its binary representation and then splits it into a list of digits
    # Note that int.to_bytes() is a python3-only function
    # In python2, you can use the struct module
    N_bin = "".join(bin(int(x))[2:] for x in str(N.to_bytes(2, 'big')))
    # Calculates the sum of the digits
    sum_of_digits = sum(map(int, N_bin))
    return bin(sum_of_digits)[2:]
