from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    if len(numbers) < 2:
        raise ValueError('numbers must have at least 2 elements')

    smallest = min(numbers)
    largest = max(numbers)

    for i in range(len(numbers)):
        numbers[i] = (numbers[i] - smallest) / (largest - smallest)

    return numbers
