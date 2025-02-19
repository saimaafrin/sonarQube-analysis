from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    sorted_numbers = sorted(numbers)
    closest_elements = (sorted_numbers[0], sorted_numbers[1])
    for i in range(1, len(sorted_numbers)):
        if abs(sorted_numbers[i] - sorted_numbers[i-1]) < abs(closest_elements[0] - closest_elements[1]):
            closest_elements = (sorted_numbers[i-1], sorted_numbers[i])
    return closest_elements
