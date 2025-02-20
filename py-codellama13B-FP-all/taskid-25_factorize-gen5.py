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
        factors.append(2)
        n //= 2
    while n % 5 == 0:
        factors.append(5)
        n //= 5
    while n % 7 == 0:
        factors.append(7)
        n //= 7
    if n > 1:
        factors.append(n)
    return factors
