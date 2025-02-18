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

    # make a set to hold all seen values
    seen = set()
    # make a dictionary to hold the first element of any triple
    triples = {}

    for i in l:
        # if the value is already in the set,
        # we know we have seen it already
        if i in seen:
            # if we have already seen a value that
            # complements it in a previous iteration,
            # and we have seen a value that is in the triple
            # that complements it, we know we have found our triple
            if i in triples and triples[i] in seen:
                return True
            else:
                # otherwise, we have not found a triple
                # yet, but we know we have seen this value
                # so we can move on
                continue
        else:
            # if this value is not in the set yet,
            # then we have found a new value that
            # complements itself
            if i in triples:
                # if we have seen this value in a previous iteration
                # then we have found a triple
                return True
            else:
                # if we have not seen this value in a previous iteration
                # then we have found a new value that complements itself
                triples[i] = 0 - i
                seen.add(i)

    # if we have made it through the loop,
    # and we have not found a triple,
    # then we know we have not found one
    return False
