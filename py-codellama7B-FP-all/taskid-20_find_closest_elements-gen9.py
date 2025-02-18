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
    min_diff_index = -1
    result_index = -1
    for i, number in enumerate(numbers):
        for j, other_number in enumerate(numbers):
            if i == j: continue
            diff = abs(number - other_number)
            if diff < min_diff:
                min_diff = diff
                result_index = i
                min_diff_index = j
    return (numbers[result_index], numbers[min_diff_index])
