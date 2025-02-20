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

    # sort and reverse
    lst.sort(reverse=True)
    # lst.reverse()
    # print(lst)
    # get min and max
    min_val = lst[0]
    max_val = lst[0]
    # print(min_val)
    # print(max_val)
    # get the middle value
    middle = len(lst) // 2
    # print(middle)
    # print(lst[middle])
    # get the middle value
    mid = lst[middle]
    # print(mid)
    # get the first value
    first_val = lst[0]
    # get the last value
    last_val = lst[-1]
    # print(last_val)
    # print(first_val)
    # find the first element not equal to mid
    idx = 0
    for i in lst:
        if i != mid:
            # print(i)
            idx = i
            # print(idx)
            break
    # print(idx)
    # print(lst[1])
    # print(lst[-1])
    # print(lst[1])
    # print(idx)
    # print(lst[-1])
    # find the last element not equal to mid
    idx = 0
    for i in lst:
        if i != mid:
            idx = i
            # print(idx)
            break
    # print(idx)
    # print(idx)
    # print(lst[1])
    # print(lst[1])
    # print(lst[-1])
    # print(lst[-1])
    # find the first element not equal to min
    idx = 0
    for i in lst:
        if i != min_val:
            idx = i
            # print(idx)
            break
    # print(idx)
    # find the last element not equal to min
    idx = 0
    for i in lst:
        if i != min_val:
            idx = i
            # print(idx)
            break
    # print(idx)
    # print(idx)
    # print(lst[1])
    # print(lst[1])
    # print(lst[-1])
    # print(lst[-1])
    # find the first element not equal to max
    idx = 0
    for i in lst:
        if i != max_val:
            idx = i
            # print(idx)
            break
    # print(idx)
    # find the last element not equal to max
    idx = 0
    for i in lst:
        if i != max_val:
            idx = i
            # print(idx)
            break
    # print(idx)
    # print(idx)
    # print(lst[1])
    # print(lst[1])
    # print(lst[-1])
    # print(lst[-1])
    # print(lst[1])
    # print(idx)
    # print(lst[-1])
    # print(idx)
    # print(idx)
    # print(idx)
    # print(lst[1])
    # print(lst[1])
    # print(lst[-1])
    # print(lst[-1])
    # print(idx)
    # print(idx)
    # print(lst[1])
    # print(lst[1])
    # print(lst[-1])
    # print(lst[-1])
    # print(idx)
    # print(idx)
    # print(idx)
    # print(lst[1])
    # print(lst[1])
    # print
