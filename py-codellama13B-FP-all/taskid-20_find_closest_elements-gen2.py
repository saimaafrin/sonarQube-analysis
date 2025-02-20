from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """


    # check list size
    if len(numbers) < 2:
        raise ValueError("Cannot find closest elements from a list with less than 2 elements")

    # find smallest and largest
    smallest = min(numbers)
    largest = max(numbers)

    # find smallest difference
    smallest_diff = largest - smallest

    # find smallest diff and store smallest, largest
    for idx1, num1 in enumerate(numbers):
        for idx2, num2 in enumerate(numbers[idx1 + 1:]):
            if num2 - num1 < smallest_diff:
                smallest_diff = num2 - num1
                smallest = num1
                largest = num2

    return (smallest, largest)
