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

    # this implementation uses a dictionary to keep track of the counts
    # of the elements in the list
    counts = {}
    for i in l:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1

    # if there are two elements that sum to zero, then the sum of their
    # counts needs to be at least two
    for i in counts:
        if counts[i] >= 2:
            return True

    return False
