from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    if len(numbers) < 2:
        raise ValueError("The list needs at least two elements.")

    old_min = min(numbers)
    old_max = max(numbers)
    old_range = old_max - old_min
    new_range = 1.0
    new_min = 0.0

    result = []

    for number in numbers:
        result.append(((number - old_min) * new_range) / old_range + new_min)

    return result
