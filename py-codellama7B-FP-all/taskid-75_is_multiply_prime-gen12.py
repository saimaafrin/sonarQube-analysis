def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    prime_numbers = get_prime_numbers(a)
    # 2 and 3 are not prime numbers, start with 5
    if len(prime_numbers) <= 2:
        return False
    # return True if the first number of the list is 2
    if prime_numbers[0] == 2:
        del prime_numbers[0]
    return len(prime_numbers) == 1
