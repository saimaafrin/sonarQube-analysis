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
        raise ValueError(f"At least two numbers must be supplied, not {len(numbers)}")

    sorted_numbers = sorted(numbers)
    closest_difference = abs(sorted_numbers[0] - sorted_numbers[1])
    closest_pair = (sorted_numbers[0], sorted_numbers[1])

    for i in range(1, len(sorted_numbers) - 1):
        current_difference = abs(sorted_numbers[i] - sorted_numbers[i + 1])
        if current_difference < closest_difference:
            closest_difference = current_difference
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])

    return closest_pair
