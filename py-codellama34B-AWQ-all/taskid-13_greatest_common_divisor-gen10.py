def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    # we need to find common divisors of a and b
    divisors = []
    for i in range(1, abs(a) + 1):
        if a % i == 0:
            divisors.append(i)

    for i in range(1, abs(b) + 1):
        if b % i == 0:
            if i in divisors:
                return i
