from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    if not len(numbers) > 1:
        raise ValueError("Expected at least 2 numbers, got %s" % len(numbers))

    min_val = min(numbers)
    max_val = max(numbers)
    scale = (1.0 / (max_val - min_val))
    return [((num - min_val) * scale) for num in numbers]
