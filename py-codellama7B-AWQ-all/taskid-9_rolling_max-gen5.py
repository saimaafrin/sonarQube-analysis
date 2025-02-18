from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result = []
    window = [0] * (len(numbers) + 1)
    window[0] = numbers[0]
    for i, x in enumerate(numbers[1:], 1):
        window[i] = max(x, window[i-1])
        result.append(window[i])
    return result
