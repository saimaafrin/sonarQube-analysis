from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # find max and min value
    min_value = min(numbers)
    max_value = max(numbers)
    # compute scale factor
    scale_factor = 1 / (max_value - min_value)
    # apply rescale
    rescaled_numbers = [ (x - min_value) * scale_factor for x in numbers ]
    # make sure the smallest value is 0 and the largest is 1
    assert min(rescaled_numbers) == 0.0
    assert max(rescaled_numbers) == 1.0
    return rescaled_numbers
