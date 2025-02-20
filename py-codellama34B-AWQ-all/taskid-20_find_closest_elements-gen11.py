from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_diff = 100
    min_indices = []

    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i+1])
        if diff < min_diff:
            min_diff = diff
            min_indices = [i, i+1]
        elif diff == min_diff:
            min_indices.append(i)
            min_indices.append(i+1)

    return (min(numbers[min_indices]), max(numbers[min_indices]))
