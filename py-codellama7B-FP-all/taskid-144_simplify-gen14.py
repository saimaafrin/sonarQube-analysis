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


    num1, denom1 = x.split("/")
    num2, denom2 = n.split("/")

    # If you can divide both numbers by a common divisor, you can simplify the expression
    divisor = _gcd(int(num1), int(denom1)) * _gcd(int(num2), int(denom2))

    num1 = int(num1) // divisor
    num2 = int(num2) // divisor
    denom1 = int(denom1) // divisor
    denom2 = int(denom2) // divisor

    return num1 * denom2 == num2 * denom1
