from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Get the difference between each pair of numbers
    differences = [abs(a - b) for a, b in zip(numbers, numbers[1:])]

    # Locate the pair that has the smallest difference
    smallest_difference_index = differences.index(min(differences))

    # Return the pair in order (smaller number, larger number)
    return numbers[smallest_difference_index], numbers[smallest_difference_index + 1]
