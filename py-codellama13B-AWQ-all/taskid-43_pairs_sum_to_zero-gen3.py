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

    # first, sort the list
    l.sort()

    # then, find the middle element of the list
    middle = len(l) // 2

    # loop over the list from 0 to the middle
    for i in range(middle):

        # find the complement to the element at i
        complement = -l[i]

        # if the complement is in the list, return True
        if complement in l:
            return True

    # if no pairs sum to zero, return False
    return False
