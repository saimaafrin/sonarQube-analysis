from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # assert(len(numbers) > 1)
    # https://stackoverflow.com/questions/31927989/how-do-i-normalize-an-array-in-numpy
    min_value = min(numbers)
    max_value = max(numbers)
    rescaled = [(x - min_value) / (max_value - min_value) for x in numbers]
    return rescaled
