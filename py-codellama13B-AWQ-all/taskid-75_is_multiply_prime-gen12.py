def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    # 2 is the only even prime
    if a == 2:
        return True
    # no other even number is prime
    if a % 2 == 0:
        return False
    
    # 3 is a prime number
    if a == 3:
        return True
    
    # no other number than 3 is prime
    if a % 3 == 0:
        return False

    return True
