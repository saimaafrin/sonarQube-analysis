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

    factors: List[int] = []
    if n == 1:
        return factors

    prime_factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for prime in prime_factors:
        count = 0
        while n % prime == 0:
            count += 1
            n //= prime
        if count != 0:
            factors.append(prime)
            factors.extend([prime] * (count - 1))
        if n == 1:
            return factors

    return factors
