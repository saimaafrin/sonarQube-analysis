from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_so_far = 0
    results = [0]
    for num in numbers:
        max_so_far = max(num, max_so_far)
        results.append(max_so_far)
    return results
