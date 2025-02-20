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

    def convert_to_binary(num):
        if num == 0:
            return '0'
        if num == 1:
            return '1'
        else:
            binary = []
            while num > 0:
                binary.append(str(num % 2))
                num = num // 2
            binary.reverse()
            return ''.join(binary)
    result = ''
    while N > 0:
        result = convert_to_binary(N % 2) + result
        N = N // 2
    return result
