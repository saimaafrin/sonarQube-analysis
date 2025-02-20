from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_at_moment = 0
    result = []
    for moment, number in enumerate(numbers):
        if number > max_at_moment:
            max_at_moment = number
        result.append(max_at_moment)
    return result
