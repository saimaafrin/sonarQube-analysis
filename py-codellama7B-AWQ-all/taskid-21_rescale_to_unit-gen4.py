from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # First, calculate the minimum and maximum values in the list
    minimum, maximum = min(numbers), max(numbers)

    # Next, calculate a scale factor that maps the minimum value to 0 and the maximum value to 1
    scale_factor = 1.0 / (maximum - minimum)

    # Finally, apply the scale factor to each number in the list
    rescaled_numbers = [scale_factor * (number - minimum) for number in numbers]
    return rescaled_numbers
\end{code}
