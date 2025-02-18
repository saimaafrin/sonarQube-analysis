from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    current_max = 0
    sequence = []
    for i, number in enumerate(numbers):
        current_max = max(current_max, number)
        sequence.append(current_max)
    return sequence
