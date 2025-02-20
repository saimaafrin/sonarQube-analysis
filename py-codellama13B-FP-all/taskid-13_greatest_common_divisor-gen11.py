def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    if a == 0 and b == 0:
        raise ValueError('Arguments cannot be both zero.')
    if a == 0:
        return b
    if b == 0:
        return a

    is_odd = lambda n: n % 2 != 0

    if is_odd(a) and is_odd(b):
        return odd_odd(a, b)
    if is_odd(a) and not is_odd(b):
        return odd_even(a, b)
    if not is_odd(a) and is_odd(b):
        return odd_even(b, a)
    return even_even(a, b)
