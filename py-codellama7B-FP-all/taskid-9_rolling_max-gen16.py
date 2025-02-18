from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    res = [None] * len(numbers)
    for i, val in enumerate(numbers):
        if i == 0:
            res[i] = val
        else:
            max_ = max(val, res[i-1])
            res[i] = max_
    return res
