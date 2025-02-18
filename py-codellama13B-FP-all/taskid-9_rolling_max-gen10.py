from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    # Initialize
    result = [numbers[0]]
    
    # Iterate
    for number in numbers[1:]:
        if number > result[-1]:
            result.append(number)
        else:
            result.append(result[-1])
    return result
