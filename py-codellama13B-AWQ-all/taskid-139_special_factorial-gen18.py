def special_factorial(n: int) -> int:
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """

    if n == 1:
        return 1
    elif n < 1:
        return ValueError("Negative number")
    else:
        return n * special_factorial(n - 1)
