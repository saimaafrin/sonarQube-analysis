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

    # code here
    x_n, n_d = x.split('/'), n.split('/')
    x_n, n_d = int(x_n[0])*int(n_d[1]), int(x_n[1])*int(n_d[0])

    if x_n % n_d == 0:
        return True
    else:
        return False
