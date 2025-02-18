from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Your code here
    smallest_abs_diff = float('inf')
    closest_pair = ()
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            current_abs_diff = abs(numbers[i]-numbers[j])
            if current_abs_diff < smallest_abs_diff:
                smallest_abs_diff = current_abs_diff
                closest_pair = (numbers[i], numbers[j])
    return closest_pair
