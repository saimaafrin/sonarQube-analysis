from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    res: List[int] = []

    for number in numbers:
        if len(res) == 0:
            res.append(number)
            continue

        last_rolling_max = res[-1]
        if number > last_rolling_max:
            res.append(number)
        else:
            res.append(last_rolling_max)

    return res
