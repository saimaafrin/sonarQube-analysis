from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    output = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[j] > numbers[i]:
                output.append(numbers[j])
                break
            else:
                output.append(numbers[i])
    return output
