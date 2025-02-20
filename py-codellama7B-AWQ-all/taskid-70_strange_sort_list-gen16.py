from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    """
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    >>> strange_sort_list([1, 2, 3, 4])
    [1, 4, 2, 3]
    >>> strange_sort_list([5, 5, 5, 5])
    [5, 5, 5, 5]
    >>> strange_sort_list([])
    []
    """

    # Your code here
    lst.sort()
    result = []
    count = 1
    while count < len(lst):
        count += 1
        result.append(lst[0])
        lst.pop(0)
        result.append(lst[-1])
        lst.pop()
    result.append(lst[0])
    return result
