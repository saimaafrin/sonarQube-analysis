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

    # Factorial using recursion
    def factorial(n: int) -> int:
        """Computes n! (n factorial)."""
        if n == 0:
            return 1
        return n * factorial(n - 1)

    # Special factorial using recursion
    def special_factorial_rec(n: int) -> int:
        """Computes n! * (n-1)! * (n-2)! * ... * 1!."""
        if n == 0:
            return 1
        return n * special_factorial_rec(n - 1)

    return factorial(n) * special_factorial_rec(n - 1)
