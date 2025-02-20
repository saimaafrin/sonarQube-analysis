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

    if n == 1:
        return []

    factors = []
    current_factor = 2

    while n > 1:
        while n % current_factor == 0:
            factors.append(current_factor)
            n //= current_factor

        if current_factor == 2:
            current_factor += 1
        else:
            current_factor += 2

    return factors
