from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    closest_elements = (numbers[0], numbers[1])
    closest_diff = abs(closest_elements[0] - closest_elements[1])
    for index in range(len(numbers) - 1):
        if abs(numbers[index] - numbers[index + 1]) < closest_diff:
            closest_elements = (numbers[index], numbers[index + 1])
            closest_diff = abs(numbers[index] - numbers[index + 1])
    return closest_elements
