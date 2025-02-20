from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    smallest_abs_difference = float("inf")
    smallest_abs_difference_indices = (-1, -1)
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers[i+1:]):
            abs_difference = abs(num1 - num2)
            if abs_difference < smallest_abs_difference:
                smallest_abs_difference = abs_difference
                smallest_abs_difference_indices = (i, i + j + 1)
    return numbers[smallest_abs_difference_indices[0]], numbers[smallest_abs_difference_indices[1]]
