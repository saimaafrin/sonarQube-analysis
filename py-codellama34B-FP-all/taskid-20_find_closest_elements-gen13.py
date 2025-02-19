from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    if len(numbers) < 2:
        raise Exception('List must have at least two elements.')
    numbers = sorted(numbers)
    smallest_diff = abs(numbers[0] - numbers[1])
    closest_elements = numbers[0], numbers[1]
    for index in range(1, len(numbers) - 1):
        current_diff = abs(numbers[index] - numbers[index + 1])
        if current_diff < smallest_diff:
            smallest_diff = current_diff
            closest_elements = numbers[index], numbers[index + 1]
    return closest_elements
