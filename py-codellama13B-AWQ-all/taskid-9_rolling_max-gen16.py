from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_sequence: List[int] = []
    for num in numbers:
        if not max_sequence or num >= max_sequence[-1]:
            max_sequence.append(num)
        else:
            while max_sequence and max_sequence[-1] < num:
                max_sequence.pop()
    return [item for item in reversed(max_sequence)]
