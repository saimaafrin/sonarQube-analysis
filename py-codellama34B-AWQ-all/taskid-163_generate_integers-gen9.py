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

    start = min(a, b)
    end = max(a, b)
    result = []
    for i in range(start, end+1):
        if len(str(i)) != len(str(end)):
            continue
        even_digits = [int(x) for x in str(i) if int(x) % 2 == 0]
        if len(even_digits) == len(str(i)):
            result.append(i)
    return sorted(result)
