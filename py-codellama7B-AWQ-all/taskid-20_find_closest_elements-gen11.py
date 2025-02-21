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
    min_diff_index_1 = min_diff_index_2 = None
    for i, number in enumerate(numbers):
        for j, number2 in enumerate(numbers[i+1:]):
            diff = abs(number - number2)
            if diff < min_diff:
                min_diff = diff
                min_diff_index_1 = i
                min_diff_index_2 = j + i + 1
    return numbers[min_diff_index_1], numbers[min_diff_index_2]
\end{code}
