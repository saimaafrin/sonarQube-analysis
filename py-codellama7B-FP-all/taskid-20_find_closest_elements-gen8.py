from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """


    # Sort the list
    numbers.sort()

    # Determine the smallest delta
    smallest_delta = float('inf')
    smallest_delta_index1 = 0
    smallest_delta_index2 = 0

    for i in range(1, len(numbers)):
        delta = abs(numbers[i] - numbers[i - 1])

        if delta < smallest_delta:
            smallest_delta = delta
            smallest_delta_index1 = i - 1
            smallest_delta_index2 = i

    return (numbers[smallest_delta_index1], numbers[smallest_delta_index2])
