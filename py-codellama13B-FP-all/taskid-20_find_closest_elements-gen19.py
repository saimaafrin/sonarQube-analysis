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
        raise ValueError('Must supply at least two numbers')

    smallest_diff = float('inf')
    closest_pair = ()
    for i, a in enumerate(numbers):
        for b in numbers[i + 1:]:
            diff = abs(a - b)
            if diff < smallest_diff:
                smallest_diff = diff
                closest_pair = (a, b)

    return closest_pair
