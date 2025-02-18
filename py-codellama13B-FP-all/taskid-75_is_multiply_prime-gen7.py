def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    if a <= 1:
        return False
    count_prime = 0
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            count_prime += 1
    return count_prime == 3
