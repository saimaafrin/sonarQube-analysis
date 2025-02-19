def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    prime_numbers = [2, 3, 5, 7]
    for prime in prime_numbers:
        if a % prime == 0:
            return True
    return False
