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

    result = []
    for n in range(a, b+1):
        n_str = str(n)
        for char in n_str:
            if int(char) % 2 == 0:
                result.append(int(char))
    return sorted(set(result))
