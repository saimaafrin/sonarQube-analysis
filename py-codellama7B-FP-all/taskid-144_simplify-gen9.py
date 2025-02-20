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

    num_x = x.split('/')[0]
    denom_x = x.split('/')[1]

    num_n = n.split('/')[0]
    denom_n = n.split('/')[1]

    # Multiply numerator of x with the denominator of n,
    # and denominator of x with the numerator of n.
    # If the result is an integer, the product evaluates to a whole number
    result_1 = int(num_x) * int(denom_n)
    result_2 = int(denom_x) * int(num_n)

    if result_1 % 1 == 0 or result_2 % 1 == 0:
        return True
    else:
        return False
