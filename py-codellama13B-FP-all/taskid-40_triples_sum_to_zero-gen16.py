from typing import List

def triples_sum_to_zero(l: List[int]) -> bool:
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """

    # sort the list in ascending order
    l.sort()

    # loop through the list
    for i in range(len(l)):
        # calculate the sum of the first two elements in the list
        # that are in front of the current index
        sum_first_two = l[i] + l[i+1]

        # loop through the remaining elements in the list
        for j in range(i+2, len(l)):
            # check if the sum of the first two elements plus the current element
            # is equal to zero
            if l[j] == -sum_first_two:
                # if the sum is equal to zero, then return True
                return True

    # if no valid triple found, then return False
    return False
