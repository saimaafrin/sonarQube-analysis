from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_diff = None
    smallest = None
    second_smallest = None

    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if min_diff is None or diff < min_diff:
            min_diff = diff
            smallest = numbers[i]
            second_smallest = numbers[i + 1]

    return (smallest, second_smallest)
