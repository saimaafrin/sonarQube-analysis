from typing import List

def search(lst: List[int]) -> int:
    """
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
    >>> search([4, 1, 2, 2, 3, 1])
    2
    >>> search([1, 2, 2, 3, 3, 3, 4, 4, 4])
    3
    >>> search([5, 5, 4, 4, 4])
    -1
    """

    counts: List[int] = [0] * len(lst)
    for i in range(len(lst)):
        if lst[i] > 0:
            counts[lst[i] - 1] += 1
    max_freq = max(counts)
    max_freq_count = counts.count(max_freq)
    if max_freq_count == 1:
        return -1
    else:
        for i in range(len(lst)):
            if counts[i] == max_freq:
                return i + 1
    return -1
