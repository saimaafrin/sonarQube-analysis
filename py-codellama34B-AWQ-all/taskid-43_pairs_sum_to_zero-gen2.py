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


    # if the input list has a length less than 2, return False
    if len(l) < 2:
        return False

    # iterate over the list, checking if the sum of
    # the current element and its complement (the
    # element of the same value but with an opposite sign)
    # is equal to 0
    for el in l:
        complement = -1 * el
        if el in l and el != complement and l.count(el) == 1 and l.count(complement) == 1:
            return True

    return False
