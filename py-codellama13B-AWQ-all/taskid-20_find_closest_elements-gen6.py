from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    diff = numbers[0] - numbers[1]
    min_diff = diff
    ind_min_diff = 0
    ind_min_diff_2 = 1
    for i in range(1, len(numbers) - 1):
        diff = numbers[i] - numbers[i + 1]
        if diff < min_diff:
            min_diff = diff
            ind_min_diff = i
            ind_min_diff_2 = i + 1
    return numbers[ind_min_diff], numbers[ind_min_diff_2]
