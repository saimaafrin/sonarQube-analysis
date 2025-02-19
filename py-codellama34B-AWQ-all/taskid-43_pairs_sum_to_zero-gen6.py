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

    # base case: an empty list does not have any pairs
    if not l:
        return False

    # base case: if the list is one element long, there is only one element
    # to pair with, so there can't be a pair that adds up to zero
    if len(l) == 1:
        return False

    # recursive case: there is at least one pair to check, and there are
    # at least two elements left to check for additional pairs
    #
    # invariant: if there is a pair in the first n elements that adds up to
    # zero, the function will return True before it checks the last element
    #
    # termination: the function will eventually return True or False
    # without checking the last element
    return l[0] + l[-1] == 0 or pairs_sum_to_zero(l[1:-1])
