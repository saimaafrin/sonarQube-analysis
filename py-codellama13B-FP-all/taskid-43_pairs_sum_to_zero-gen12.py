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


    # check for size < 2
    if len(l) < 2:
        return False

    # make a dictionary of counts of elements
    counts = {}
    for element in l:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1

    # search for two elements that sum to zero
    for element in counts:
        complement = -element
        if complement in counts and counts[complement] > 0 and counts[element] > 0:
            return True

    return False
