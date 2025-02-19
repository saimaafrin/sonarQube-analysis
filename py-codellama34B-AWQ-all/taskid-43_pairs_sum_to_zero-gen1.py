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

    if len(l) < 2:
        return False

    # O(n) time and space
    # seen_nums = set()
    # for num in l:
    #     complement = -1 * num
    #     if complement in seen_nums:
    #         return True
    #     seen_nums.add(num)
    # return False

    # O(n log n) time and space
    l.sort()
    for i in range(len(l) - 1):
        complement = -1 * l[i]
        j = len(l) - 1
        while l[i] + l[j] > 0:
            j -= 1
        if j > i and l[i] + l[j] == 0:
            return True
    return False
