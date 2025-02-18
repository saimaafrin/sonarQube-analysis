from typing import List

def sort_array(array: List[int]) -> List[int]:
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    >>> sort_array([])
    []
    >>> sort_array([5])
    [5]
    >>> sort_array([2, 4, 3, 0, 1, 5])
    [0, 1, 2, 3, 4, 5]
    >>> sort_array([2, 4, 3, 0, 1, 5, 6])
    [6, 5, 4, 3, 2, 1, 0]
    """


    # 1. 决策
    # 在排序之前，需要先决定怎么决定排序方式。
    # 在本题中，我们需要根据数组的第一个元素和最后一个元素的和，决定排序的方式。
    # 如果这个和是奇数，那么我们需要排序为升序。如果和是偶数，那么我们需要排序为降序。
    # 所以我们需要首先获取这个和，然后再根据这个和来决定排序的方式。

    # 2. 决策执行顺序
    # 在本题中，我们不需要执行任何决策的顺序。
    # 所以我们可以直接按照下面的顺序进行：
    # 1. 获取和
    # 2. 排序
    # 3. 返回排序后的数组

    # 3. 写代码
    # 如果和是奇数，那么我们需要排序为升序
    # 如果和是偶数，那么我们需要排序为降序
    # 所以我们可以使用 sorted 函数来对数组排序
    # 然后再根据和的奇偶性来判断是否需要对数组进行逆序排序

    sum_first_last_value = sum(array)
    is_odd = sum_first_last_value % 2

    # 排序
    sorted_array = sorted(array)

    # 逆序排序
    if not is_odd:
        sorted_array.reverse()

    return sorted_array
