from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    min_value = min(numbers)
    max_value = max(numbers)
    diff = max_value - min_value

    if diff == 0:
        diff = 1.0

    return [float(number - min_value) / diff for number in numbers]
