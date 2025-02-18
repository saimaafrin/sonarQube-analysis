from typing import List

def smallest_change(arr: List[int]) -> int:
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    >>> smallest_change([1, 2, 3, 5, 4, 7, 9, 6])
    4
    >>> smallest_change([1, 2, 3, 4, 3, 2, 2])
    1
    >>> smallest_change([1, 2, 3, 2, 1])
    0
    """

    if len(arr) <= 1:
        return 0

    # get the counts of each element
    counts = {}
    for element in arr:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1

    # check for odd or even number of elements
    if len(counts) % 2 == 0:
        return 1
    else:
        count_of_most_frequent_element = 0
        for element in counts:
            if counts[element] > count_of_most_frequent_element:
                count_of_most_frequent_element = counts[element]

        if count_of_most_frequent_element % 2 == 0:
            return 1
        else:
            return 2
