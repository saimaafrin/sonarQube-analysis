from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    assert len(numbers) > 0, "At least one integer must be provided"

    result = []
    max_until_now = 0

    for i in range(len(numbers)):
        if numbers[i] >= max_until_now:
            max_until_now = numbers[i]

        result.append(max_until_now)

    return result
