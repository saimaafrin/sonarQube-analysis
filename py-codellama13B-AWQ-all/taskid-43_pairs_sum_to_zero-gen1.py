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

    # initialize a set
    s = set()
    # iterate over the list
    for i in l:
        # check if the negative of i is in the set
        if -i in s:
            # if it is return true
            return True
        # add i to the set
        s.add(i)
    # if we reach this point the set has not been updated
    # so the elements cannot be paired
    return False
