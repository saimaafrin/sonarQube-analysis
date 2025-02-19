from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result: List[int] = []
    if len(numbers) == 0:
        return result
    else:
        max_so_far = numbers[0]
        result.append(max_so_far)
        for i in range(1, len(numbers)):
            if numbers[i] > max_so_far:
                max_so_far = numbers[i]
            result.append(max_so_far)
        return result
