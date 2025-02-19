def is_simple_power(x: int, n: int) -> bool:
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    >>> is_simple_power(1, 4)
    True
    >>> is_simple_power(2, 2)
    True
    >>> is_simple_power(8, 2)
    True
    >>> is_simple_power(3, 2)
    False
    >>> is_simple_power(3, 1)
    False
    >>> is_simple_power(5, 3)
    False
    """

    if n == 1:
        return True

    if n < 1 or n % 2 == 0:
        return False

    while n > 1:
        n /= 2

    return n == 1
