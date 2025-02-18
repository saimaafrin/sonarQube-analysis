def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    # Implement your solution here
    if a == 0:
        return False
    p = []
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            p.append(i)
    if len(p) == 3:
        return True
    else:
        return False
