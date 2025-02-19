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

    x_parts = x.split('/')
    n_parts = n.split('/')

    # Simplify both fractions to reduce the common denominator
    gcd = __gcd(int(x_parts[0]), int(x_parts[1]))
    x_parts[0] = str(int(x_parts[0]) // gcd)
    x_parts[1] = str(int(x_parts[1]) // gcd)

    gcd = __gcd(int(n_parts[0]), int(n_parts[1]))
    n_parts[0] = str(int(n_parts[0]) // gcd)
    n_parts[1] = str(int(n_parts[1]) // gcd)

    return x_parts[1] == n_parts[0]
