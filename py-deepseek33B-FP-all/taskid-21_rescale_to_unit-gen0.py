from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    if len(numbers) < 2:
        raise ValueError('Cannot rescale a list of less than two numbers')
    if any(n < 0 for n in numbers):
        raise ValueError('Cannot rescale a list of negative numbers')
    min_n = min(numbers)
    max_n = max(numbers)
    return [(n - min_n) / (max_n - min_n) for n in numbers]
