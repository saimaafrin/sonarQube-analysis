def simplify(x: str, n: str) -> bool:
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    >>> simplify('1/5', '5/1')
    True
    >>> simplify('1/6', '2/1')
    False
    >>> simplify('7/10', '10/2')
    False
    """

    x_num, x_denom = x.split('/')
    n_num, n_denom = n.split('/')

    gcd = 1
    for i in range(1, max(int(x_num), int(n_num)) + 1):
        if x_num % i == 0 and n_num % i == 0:
            gcd = i

    x_num, x_denom = int(x_num), int(x_denom)
    n_num, n_denom = int(n_num), int(n_denom)

    x_num //= gcd
    x_denom //= gcd
    n_num //= gcd
    n_denom //= gcd

    return x_num * n_denom == x_denom * n_num
