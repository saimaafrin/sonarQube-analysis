from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    numbers = sorted(numbers)
    left = 0
    right = 1
    closest_pair = (numbers[left], numbers[right])
    for i in range(1, len(numbers)):
        left = i
        right = i + 1
        if abs(numbers[left] - numbers[right]) < abs(closest_pair[0] - closest_pair[1]):
            closest_pair = (numbers[left], numbers[right])
    return closest_pair
