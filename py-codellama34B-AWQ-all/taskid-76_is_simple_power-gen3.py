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

    if not isinstance(x, int):
        raise TypeError("Invalid type")
    if not isinstance(n, int):
        raise TypeError("Invalid type")
    if x < 0:
        raise ValueError("Invalid number")

    if x == 0:
        return True
    if n == 0:
        return False

    while x > 1:
        x, remainder = divmod(x, n)
        if remainder != 0:
            return False
    return True
