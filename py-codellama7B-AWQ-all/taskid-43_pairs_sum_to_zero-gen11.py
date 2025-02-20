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


    # Hint: The algorithm is very simple. It's a dictionary comprehension
    # that maps each element in the list to its index.
    # Then, for each element, check if the sum of that element with
    # any other element is zero.
    l_map = {element: i for i, element in enumerate(l)}

    for i, element in enumerate(l):
        if l_map[element] == i:
            continue
        if l[i] + element == 0:
            return True

    return False
