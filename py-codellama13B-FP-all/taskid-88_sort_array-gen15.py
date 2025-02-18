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


    def _swap(array: List[int], i: int, j: int) -> List[int]:
        array[i], array[j] = array[j], array[i]

    def _sort(array: List[int], i: int, j: int) -> List[int]:
        if i >= j:
            return array
        mid = (i + j) // 2
        _sort(array, i, mid)
        _sort(array, mid + 1, j)
        _merge(array, i, mid, j)

    def _merge(array: List[int], i: int, mid: int, j: int) -> List[int]:
        tmp = []
        while i <= mid and mid + 1 <= j:
            if sum(array[i], array[j]) % 2 == 1:
                if array[i] < array[j]:
                    _swap(array, i, mid + 1)
                    _swap(array, i, j)
                else:
                    _swap(array, mid + 1, j)
                    _swap(array, i, j)
            elif sum(array[i], array[j]) % 2 == 0:
                if array[i] > array[j]:
                    _swap(array, i, mid + 1)
                    _swap(array, i, j)
                else:
                    _swap(array, mid + 1, j)
                    _swap(array, i, j)
            i += 1
            j -= 1

        if i <= mid:
            while i <= mid:
                tmp.append(array[i])
                i += 1

        if mid + 1 <= j:
            while mid + 1 <= j:
                tmp.append(array[mid + 1])
                mid += 1

        if len(tmp) > 0:
            array[i:j + 1] = tmp

    size = len(array)
    if size <= 1:
        return array

    _sort(array, 0, size - 1)
    return array
