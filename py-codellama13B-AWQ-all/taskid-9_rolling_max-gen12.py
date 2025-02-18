from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    maximum = numbers[0]
    max_list = []
    for number in numbers:
        if number > maximum:
            maximum = number
        max_list.append(maximum)
    return max_list
