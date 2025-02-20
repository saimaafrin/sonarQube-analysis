from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_value = 0
    rolling_max_seq = []
    for element in numbers:
        if element > max_value:
            max_value = element
        rolling_max_seq.append(max_value)
    return rolling_max_seq
