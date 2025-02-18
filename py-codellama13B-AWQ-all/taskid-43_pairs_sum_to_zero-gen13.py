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
    # sort the list in ascending order
    l.sort()
    # loop through the list from left to right
    # find if the sum of two elements is equal to zero
    for i, num in enumerate(l):
        # if the sum of two elements is equal to zero, return True
        if num == 0:
            return True
        # if the sum of two elements is greater than zero,
        # the element must be in the right half of the list
        elif num > 0:
            # find the corresponding element in the right half of the list
            right_num = l[-i]
            # if the sum of two elements is equal to zero, return True
            if num + right_num == 0:
                return True
    # no such elements exist
    return False
