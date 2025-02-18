from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """


    output: List[int] = []

    for i in range(len(numbers)):
        if i == 0:
            output.append(numbers[i])
        else:
            if numbers[i] > output[-1]:
                output.append(numbers[i])
            else:
                output.append(output[-1])

    return output
