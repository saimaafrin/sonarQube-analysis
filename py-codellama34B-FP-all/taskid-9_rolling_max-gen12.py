from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_element = 0
    rolling_max_list: List[int] = []
    for number in numbers:
        if number > max_element:
            max_element = number
        rolling_max_list.append(max_element)

    return rolling_max_list
