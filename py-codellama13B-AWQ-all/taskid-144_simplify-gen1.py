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


    # 1. Convert to float to avoid precision issues
    x_num, x_den = x.split("/")
    n_num, n_den = n.split("/")
    x = float(x_num) / float(x_den)
    n = float(n_num) / float(n_den)

    # 2. Multiply x by n
    product = x * n

    # 3. Check if the product is a whole number
    if product % 1 == 0:
        return True
    else:
        return False
