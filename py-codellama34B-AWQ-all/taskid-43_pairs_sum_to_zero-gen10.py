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

    # check if list length is greater than 1
    if len(l) > 1:
        # iterate through list
        for i in range(len(l)):
            # iterate through rest of list starting from i+1
            for j in range(i+1, len(l)):
                # if elements add up to 0, return True
                if l[i] + l[j] == 0:
                    return True
        # if no pairs add up to zero, return False
        return False
    # if list length is less than 1, return False
    return False
