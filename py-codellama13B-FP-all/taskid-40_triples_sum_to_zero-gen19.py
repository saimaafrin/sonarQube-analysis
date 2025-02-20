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

    # This is a good use case for a set.  We can remove duplicates
    # by storing elements in a set.  We can also check for the number
    # of elements in a set in O(1) time.
    s = set(l)

    # If the length of the set is less than 3, we can't have a triple.
    if len(s) < 3:
        return False

    # We could also have a triple if the sum of the first two elements
    # is equal to the third element.
    for x in s:
        for y in s:
            if x + y in s:
                return True

    # If we made it to this point, we didn't find a triple.
    return False
