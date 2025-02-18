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

    n1, d1 = x.split('/')
    n2, d2 = n.split('/')
    if d1 == '1':
        if d2 == '1':
            return True
        else:
            return False
    else:
        if d2 == '1':
            return False
        else:
            if (n1 * int(d2)) == (n2 * int(d1)):
                return True
            else:
                return False
