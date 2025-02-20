def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    if a <= 2:
        return False
    prime = [2]
    for i in range(3, 100, 2):
        for j in prime:
            if i % j == 0:
                break
        else:
            prime.append(i)
    for i in prime:
        for j in prime:
            if a % (i * j) == 0:
                return True
    return False
