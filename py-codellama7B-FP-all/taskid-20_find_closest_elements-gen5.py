from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """



    # Find smallest difference between two numbers
    smallest_difference = abs(numbers[1] - numbers[0])
    smallest_difference_index = 0
    for i in range(1, len(numbers)):
        difference = abs(numbers[i] - numbers[i-1])
        if difference < smallest_difference:
            smallest_difference = difference
            smallest_difference_index = i

    return (numbers[smallest_difference_index - 1], numbers[smallest_difference_index])
