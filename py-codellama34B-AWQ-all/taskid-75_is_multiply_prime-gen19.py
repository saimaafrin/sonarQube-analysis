def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    if a > 100:
        raise ValueError("Input must be less then 100")

    prime_factors = []
    for i in range(2, a):
        if a % i == 0:
            prime_factors.append(i)

    if len(prime_factors) != 2:
        return False

    return True
