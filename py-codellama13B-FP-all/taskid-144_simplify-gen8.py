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

    x_n, x_d = map(int, x.split('/'))
    n_n, n_d = map(int, n.split('/'))
    # This is the only one that doesn't give the correct answer
    return x_n * n_d % x_d == 0

    # Other possible implementations:
    return (x_n * n_n) % (x_d * n_d) == 0
    return (x_n * n_d) % x_d == 0
    return (n_n * x_d) % n_d == 0
