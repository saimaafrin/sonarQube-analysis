from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    >>> generate_integers(2, 8)
    [2, 4, 6, 8]
    >>> generate_integers(8, 2)
    [2, 4, 6, 8]
    >>> generate_integers(10, 14)
    []
    """

    # 2. Use a list comprehension to generate all integers between `a` and `b`.
    # 3. Filter out all odd integers and all integers greater than 9.
    # 4. Sort the remaining integers and return them.
    return sorted([i for i in range(min(a, b), max(a, b)+1) if i % 2 == 0 and i <= 9])
