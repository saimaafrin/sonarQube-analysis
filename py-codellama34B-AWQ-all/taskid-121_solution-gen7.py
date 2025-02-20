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

    # Initialize variables
    odd_sum: int = 0
    idx: int = 0

    # Iterate over each element in the list
    for i in lst:
        # If the element is odd and the index is even, add it to the sum
        if i % 2 == 1 and idx % 2 == 0:
            odd_sum += i
        # Increment the index for the next iteration
        idx += 1

    return odd_sum
