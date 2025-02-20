from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_diff = float('inf')
    min_diff_idx = 0
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            diff = numbers[j] - numbers[i]
            if diff < min_diff:
                min_diff = diff
                min_diff_idx = i
                j_idx = j
    return numbers[min_diff_idx], numbers[j_idx]
