from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    max_value, min_value = max(numbers), min(numbers)
    if max_value == min_value:
        return [0] * len(numbers)
    return [(number - min_value) / (max_value - min_value) for number in numbers]
