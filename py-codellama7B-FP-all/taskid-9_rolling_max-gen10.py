from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_so_far = -1
    rolling_max_list = []
    for n in numbers:
        max_so_far = max(n, max_so_far)
        rolling_max_list.append(max_so_far)
    return rolling_max_list
