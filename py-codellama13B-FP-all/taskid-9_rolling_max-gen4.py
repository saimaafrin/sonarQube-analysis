from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    if len(numbers) < 2:
        return numbers

    max_so_far = max(numbers[0], numbers[1])
    result = [max_so_far, max(numbers[1], max_so_far)]
    for i in range(2, len(numbers)):
        current_max = max(result[i-1], numbers[i])
        result.append(current_max)
    return result
