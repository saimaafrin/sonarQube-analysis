from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max: List[int] = []

    for number in numbers:
        if rolling_max:
            rolling_max.append(max(rolling_max[-1], number))
        else:
            rolling_max.append(number)

    return rolling_max
