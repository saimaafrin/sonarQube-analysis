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
    # start from 2 and keep dividing until we reach 1
    while n != 1:
        factor = 2
        # check how many times we can divide before we get to 1
        while n % factor == 0:
            factors.append(factor)
            n //= factor
            factor += 1
    return factors
