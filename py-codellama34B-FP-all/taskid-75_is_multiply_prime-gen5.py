def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    if a < 3:
        return False

    # find prime numbers
    prime_numbers = []
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            prime_numbers.append(i)
            prime_numbers.append(a // i)
            break
    else:
        return False
    
    # find multiply
    for i in range(2, a):
        if a % i == 0:
            if (a // i) in prime_numbers:
                return True
    return False
