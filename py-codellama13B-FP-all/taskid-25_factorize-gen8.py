from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """


    if n < 2:
        return []

    # find first prime number factor
    prime_factor = 2
    while n % prime_factor != 0:
        prime_factor += 1

    factors = [prime_factor]
    while prime_factor * prime_factor <= n:
        while n % prime_factor == 0:
            n //= prime_factor
            factors.append(prime_factor)

    if n > 1:
        factors.append(n)

    return factors
