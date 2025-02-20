from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    assert len(numbers) > 1
    # find the min and max
    min_val = min(numbers)
    max_val = max(numbers)
    # calculate the scaling factor
    scaling_factor = 1.0 / (max_val - min_val)
    # rescale the numbers
    return [(x - min_val) * scaling_factor for x in numbers]
\end{code}
