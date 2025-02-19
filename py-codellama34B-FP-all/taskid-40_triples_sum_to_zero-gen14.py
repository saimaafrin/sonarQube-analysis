from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """

    if len(l) < 3:
        return False

    for idx in range(len(l)):
        first = l[idx]
        for idx2 in range(idx + 1, len(l)):
            second = l[idx2]
            for idx3 in range(idx2 + 1, len(l)):
                third = l[idx3]
                if first + second + third == 0:
                    return True
    return False
