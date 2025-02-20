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
    closest = (sorted_numbers[0], sorted_numbers[1])

    for i in range(2, len(sorted_numbers)):
        current = (sorted_numbers[i-1], sorted_numbers[i])

        if abs(current[0] - current[1]) < abs(closest[0] - closest[1]):
            closest = current

    return closest
