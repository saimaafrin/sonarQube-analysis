def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """


    def gcd_recursive(a: int, b: int) -> int:
        if b == 0:
            return a
        else:
            return gcd_recursive(b, a % b)

    return gcd_recursive(a, b)
