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

    N_binary = ''

    # convert to binary
    while N > 0:
        N_binary = str(N % 2) + N_binary
        N = N // 2

    # get sum of the binary
    sum_binary = '0'
    for i in range(len(N_binary)):
        sum_binary = str(int(sum_binary) + int(N_binary[i]))
    return sum_binary
