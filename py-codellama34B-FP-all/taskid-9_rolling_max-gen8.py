from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """


    assert numbers, "Provided list should not be empty"
    rolling_maximum = [numbers[0]]
    for idx, number in enumerate(numbers):
        if number > rolling_maximum[-1]:
            rolling_maximum.append(number)
        else:
            rolling_maximum.append(rolling_maximum[-1])
    return rolling_maximum
