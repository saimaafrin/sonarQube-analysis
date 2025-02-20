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


    def evaluate(frac1, frac2):
        num1, denom1 = map(int, frac1.split('/'))
        num2, denom2 = map(int, frac2.split('/'))
        return (num1 * num2) // (denom1 * denom2)

    return evaluate(x, n) in range(1, 10)
