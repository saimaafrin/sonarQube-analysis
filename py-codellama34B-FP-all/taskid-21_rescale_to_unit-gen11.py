from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    if len(numbers) < 2:
        raise ValueError("List has to contain at least two elements.")
    min_val = min(numbers)
    max_val = max(numbers)
    denominator = max_val - min_val
    if denominator == 0:
        raise ValueError("All numbers in the list are the same.")
    rescaled_list = []
    for n in numbers:
        rescaled_list.append((n - min_val) / denominator)
    return rescaled_list
