def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    if a < 100:
        isPrime = lambda n: n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

        if isPrime(a):
            return True
        else:
            a = a - 1

        while not isPrime(a) and a >= 1:
            a = a - 1

        if a == 1:
            return False

        for i in range(1, a):
            if isPrime(i) and isPrime(a - i):
                return True

    return False
