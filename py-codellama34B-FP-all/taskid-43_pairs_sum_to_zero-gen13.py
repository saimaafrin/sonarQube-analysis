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


    # check the input is a list
    if not isinstance(l, list):
        raise TypeError("Input must be a list")

    # check the list has at least two elements
    if len(l) < 2:
        return False

    # check the list has two distinct elements that sum to zero
    for i, x in enumerate(l[:-1]):
        for y in l[i+1:]:
            if x + y == 0:
                return True

    return False
