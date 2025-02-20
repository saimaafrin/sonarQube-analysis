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

    # Write your code here
    if len(lst) == 0:
        return lst
    else:
        min_num = lst[0]
        max_num = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > max_num:
                max_num = lst[i]
            elif lst[i] < min_num:
                min_num = lst[i]
        lst.remove(max_num)
        lst.remove(min_num)
        lst.insert(0, min_num)
        lst.append(max_num)
        return lst
