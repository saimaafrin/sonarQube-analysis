from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    numbers.sort()
    smallest_diff = None
    smallest_diff_indices = None
    for i in range(len(numbers) - 1):
        current_diff = numbers[i + 1] - numbers[i]
        if smallest_diff is None or smallest_diff > current_diff:
            smallest_diff = current_diff
            smallest_diff_indices = i, i + 1
    return numbers[smallest_diff_indices[0]], numbers[smallest_diff_indices[1]]
\end{code}
