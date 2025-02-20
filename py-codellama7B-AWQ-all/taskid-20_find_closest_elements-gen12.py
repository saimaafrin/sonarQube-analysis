from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    smallest_difference = None
    closest_pair = None
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            difference = abs(numbers[j] - numbers[i])
            if smallest_difference is None or difference < smallest_difference:
                smallest_difference = difference
                closest_pair = (numbers[i], numbers[j])
    return closest_pair
