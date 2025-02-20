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

    # if there are no two elements in the list that sum to zero,
    # return False
    if len(l) < 2:
        return False
    
    # otherwise, for each element in the list, check
    # if it's complement (its negative value) is in the list
    # (if the complement is in the list, then there is a pair
    # of distinct elements in the list that sum to zero)
    for i in range(len(l)):
        if -l[i] in l:
            return True
    return False
