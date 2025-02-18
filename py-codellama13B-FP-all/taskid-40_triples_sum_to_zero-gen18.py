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

    # create a set of unique elements from the list
    u = set(l)
    # initialize a bool to store whether we found a triplet or not
    found_triple = False

    # iterate over all elements in the unique set
    for i in u:
        # find the complement of i (the other two elements that sum to zero)
        j = -i
        # check if j is in the set
        if j in u:
            # j is in the set, so find the third element
            k = i + j
            # check if k is in the set
            if k in u:
                # k is in the set, so we found our triplet!
                found_triple = True
                break

    return found_triple
