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

    # get all pairs of distinct elements in l
    pairs = [(l[i], l[j]) for i in range(len(l)) for j in range(i + 1, len(l)) if l[i] != l[j]]

    # get all triples of distinct elements in l
    triples = [(p[0], l[k]) for p in pairs for k in range(len(l)) if l[k] != p[0] and l[k] != p[1]]

    # check if there are any triples of distinct elements that sum to zero
    for t in triples:
        if t[0] + t[1] == 0:
            return True

    # if we get here, there are no triples of distinct elements that sum to zero
    return False
