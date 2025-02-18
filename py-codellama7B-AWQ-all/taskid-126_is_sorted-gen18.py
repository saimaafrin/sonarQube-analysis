from typing import List

def is_sorted(lst: List[int]) -> bool:
    """
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    >>> is_sorted([5])
    True
    >>> is_sorted([1, 2, 3, 4, 5])
    True
    >>> is_sorted([1, 3, 2, 4, 5])
    False
    >>> is_sorted([1, 2, 3, 4, 5, 6])
    True
    >>> is_sorted([1, 2, 3, 4, 5, 6, 7])
    True
    >>> is_sorted([1, 3, 2, 4, 5, 6, 7])
    False
    >>> is_sorted([1, 2, 2, 3, 3, 4])
    True
    >>> is_sorted([1, 2, 2, 2, 3, 4])
    False
    """


    # Solution 1
    return lst == sorted(lst)

    # Solution 2
    # for i in range(len(lst) - 1):
    #     if lst[i] > lst[i + 1]:
    #         return False
    # return True

    # Solution 3
    # for i in range(len(lst)):
    #     if i > 0 and lst[i] < lst[i - 1]:
    #         return False
    # return True

    # Solution 4
    # return lst == list(sorted(set(lst)))

    # Solution 5
    # return lst == list(reversed(sorted(lst)))
