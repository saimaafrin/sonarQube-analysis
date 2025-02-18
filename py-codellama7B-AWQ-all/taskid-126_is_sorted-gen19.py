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

    # Check if list is sorted.
    sorted_list = sorted(lst)
    if lst == sorted_list:
        # Check if list has more than 1 duplicate.
        unique_values = []
        for i in lst:
            if i not in unique_values:
                unique_values.append(i)
        if len(unique_values) == len(lst):
            return True
        else:
            return False
    else:
        return False
\end{code}
