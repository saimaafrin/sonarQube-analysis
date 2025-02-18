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

    factors = []
    while n % 2 == 0:
        n //= 2
        factors.append(2)
    while n % 3 == 0:
        n //= 3
        factors.append(3)
    i = 5
    while i * i <= n:
        if n % i == 0:
            n //= i
            factors.append(i)
        i += 2
    if n > 1:
        factors.append(n)
    return factors
