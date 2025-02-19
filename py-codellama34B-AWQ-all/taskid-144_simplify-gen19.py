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

    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    def fraction(x: str) -> tuple[int, int]:
        num, denom = x.split('/')
        num, denom = int(num), int(denom)
        g = gcd(num, denom)
        return num // g, denom // g

    num_x, denom_x = fraction(x)
    num_n, denom_n = fraction(n)

    num = num_x * num_n
    denom = denom_x * denom_n

    return num % denom == 0
