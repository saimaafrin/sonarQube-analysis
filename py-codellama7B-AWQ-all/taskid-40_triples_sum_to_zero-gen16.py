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

    # -------------------------------------------------------------------------
    #  YOUR CODE HERE
    #  If you have trouble with this question, you can look at the
    #  examples in the `solutions` directory.
    #  You should check the tests in `test_triples_sum_to_zero.py` for
    #  more examples.
    # -------------------------------------------------------------------------
    seen = set()
    for num in l:
        if num in seen:
            continue
        seen.add(num)
        if num == 0:
            return True
        for other in l:
            if num + other == 0:
                return True
    return False
