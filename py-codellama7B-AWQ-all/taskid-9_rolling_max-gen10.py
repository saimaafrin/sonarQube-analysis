from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling = []
    rolling.append(numbers[0])

    for i in range(1, len(numbers)):
        if numbers[i] > rolling[-1]:
            rolling.append(numbers[i])
        else:
            rolling.append(rolling[-1])

    return rolling
