from typing import List

def pairs_sum_to_zero(l: List[int]) -> bool:
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """

    if len(l) < 2:
        return False

    l.sort()
    i = 0
    j = len(l) - 1
    while i != j:
        if l[i] + l[j] == 0:
            return True
        if l[i] + l[j] > 0:
            j -= 1
        else:
            i += 1

    return False
