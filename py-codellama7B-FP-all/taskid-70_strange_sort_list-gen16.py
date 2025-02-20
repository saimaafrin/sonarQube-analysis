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
    # Hint: Use a while loop to get minimum and maximum of the remaining values
    min = 0
    max = 0
    result = []
    while len(lst) != 0:
        min = lst[0]
        max = lst[0]
        for num in lst:
            if num < min:
                min = num
            if num > max:
                max = num
        result.append(min)
        result.append(max)
        lst.remove(min)
        lst.remove(max)
    return result
