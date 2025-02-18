def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """


    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n % 2 == 0:
            return n == 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_multiply_of_3_prime(n: int) -> bool:
        if is_prime(n):
            return True
        if is_prime(n // 2):
            return True
        if is_prime(n // 3):
            return True
        return False

    return is_multiply_of_3_prime(a)
