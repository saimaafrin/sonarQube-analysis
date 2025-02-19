from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    min_ = min(numbers)
    max_ = max(numbers)
    if min_ == max_:
        return [0.0] * len(numbers)
    return [(number - min_) / (max_ - min_) for number in numbers]
