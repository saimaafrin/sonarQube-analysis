from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_so_far = -1
    result = []
    for num in numbers:
        if max_so_far < num:
            max_so_far = num
        result.append(max_so_far)
    return result
