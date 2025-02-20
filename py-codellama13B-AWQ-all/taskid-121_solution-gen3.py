from typing import List

def solution(lst: List[int]) -> int:
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    >>> solution([5, 8, 7, 1])
    12
    >>> solution([3, 3, 3, 3, 3])
    9
    >>> solution([30, 13, 24, 321])
    0
    """

    # convert list to a string and split it by commas
    s = str(lst).replace("[", "").replace("]", "").split(", ")
    # declare variables
    odd_sum = 0
    idx = 0
    # iterate over each element in the list
    for i in s:
        # add the element to odd_sum if the index is even and the element is odd
        if idx % 2 == 0 and int(i) % 2 != 0:
            odd_sum += int(i)
        idx += 1
    # return the sum of all odd numbers in even positions
    return odd_sum
