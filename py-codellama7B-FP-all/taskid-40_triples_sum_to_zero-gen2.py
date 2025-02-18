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

    seen = set()
    for e in l:
        # If e is zero, we're done
        if e == 0:
            return True
        # If e is negative, subtract its absolute value from each element
        # in seen.
        elif e < 0:
            for x in seen:
                # If the sum of e and x is zero, we're done
                if x - e == 0:
                    return True
        # If e is positive, add it to each element in seen
        else:
            for x in seen:
                # If the sum of e and x is zero, we're done
                if x + e == 0:
                    return True
        seen.add(e)

    return False
