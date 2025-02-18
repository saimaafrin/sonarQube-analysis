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


    # we need three distinct elements
    if len(l) < 3:
        return False

    # we use a set to keep track of the elements we've seen so far
    seen = set()

    # if we see an element that is not in the set
    # add it to the set
    for e in l:
        if e not in seen:
            seen.add(e)
        # if the sum of the element and the current element is zero
        # return True
        elif (e + e) == 0:
            return True
    return False
