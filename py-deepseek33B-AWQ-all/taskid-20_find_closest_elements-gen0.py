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
    smallest_difference = None
    closest_elements = None
    for i in range(len(sorted_numbers) - 1):
        difference = sorted_numbers[i + 1] - sorted_numbers[i]
        if smallest_difference is None or difference < smallest_difference:
            smallest_difference = difference
            closest_elements = sorted_numbers[i], sorted_numbers[i + 1]
    return closest_elements
