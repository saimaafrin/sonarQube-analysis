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
        raise ValueError('Need at least two numbers')

    smallest_distance = float('inf')
    smallest_number = numbers[0]
    largest_number = numbers[1]
    for index, number in enumerate(numbers[1:]):
        if number - smallest_number < smallest_distance:
            smallest_distance = number - smallest_number
            smallest_number = number
            largest_number = numbers[index]
        elif number - largest_number < smallest_distance:
            smallest_distance = number - largest_number
            smallest_number = numbers[index]
            largest_number = number

    return smallest_number, largest_number
