from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    closest_elements: Tuple[float, float] = (0.0, 0.0)
    smallest_difference = float("inf")
    for i in range(len(numbers) - 1):
        current_difference = abs(numbers[i] - numbers[i + 1])
        if current_difference < smallest_difference:
            smallest_difference = current_difference
            closest_elements = (numbers[i], numbers[i + 1])
        elif current_difference == smallest_difference:
            closest_elements = min(numbers[i], numbers[i + 1]), max(numbers[i], numbers[i + 1])
    return closest_elements
