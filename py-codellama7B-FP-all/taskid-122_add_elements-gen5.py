from typing import List

def add_elements(arr: List[int], k: int) -> int:
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

    >>> add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4)
    24

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """


    # 1. 计算前 k 个数中最大的两位数
    # 2. 取出前 k 个数中较小的一个数
    # 3. 将前 k 个数中最大的两位数与小数相加

    max_val = -1
    min_val = -1

    for i in range(k):
        if arr[i] > max_val:
            max_val = arr[i]

    for i in range(k):
        if arr[i] < max_val and (min_val < 0 or arr[i] < min_val):
            min_val = arr[i]

    if min_val < 0:
        return sum(arr[:k])

    return sum(arr[:k]) - min_val + max_val
