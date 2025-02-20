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

    # A brute-force approach that runs in O(n^3) time
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         for k in range(j+1, len(l)):
    #             if l[i] + l[j] + l[k] == 0:
    #                 return True
    # return False

    # A faster approach that runs in O(n^2) time
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         complement = -l[i] - l[j]
    #         if complement in l:
    #             return True
    # return False

    # An optimized version of the above that runs in O(n^2) time
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         complement = -l[i] - l[j]
    #         if complement in l and l.index(complement) > j:
    #             return True
    # return False

    # An optimized version of the above that runs in O(n) time
    nums = set(l)
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            complement = -l[i] - l[j]
            if complement in nums:
                return True
    return False
