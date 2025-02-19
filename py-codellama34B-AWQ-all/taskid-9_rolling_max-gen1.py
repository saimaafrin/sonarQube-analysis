from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    # Initialize rolling maximum variable as 0
    max_till_now = 0
    # Initialize result
    result = []
    # Iterate the list
    for num in numbers:
        # Compare number with rolling maximum found until current moment
        if num > max_till_now:
            # If number is greater than current maximum, it becomes new rolling maximum
            max_till_now = num
        # Append rolling maximum to result
        result.append(max_till_now)
    # Return result
    return result
