def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Initialize a list of prime numbers less than n
    primes = [2]
    # Initialize a list of numbers less than n that have not been eliminated
    numbers = list(range(3, n + 1))
    # While there are still numbers in the list, eliminate multiples of primes
    while numbers:
        p = primes[-1]
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[i] % p == 0:
                numbers.pop(i)
    # The largest prime factor is the last prime number
    return primes[-1]
