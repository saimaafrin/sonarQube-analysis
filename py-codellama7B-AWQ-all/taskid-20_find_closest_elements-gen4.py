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
    # We assume the list of numbers is non-empty and at least two long
    assert len(numbers) > 1
    # We will find the min and max of the list of numbers
    min_index, max_index = 0, 0
    min_value, max_value = numbers[0], numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min_value:
            min_index = i
            min_value = numbers[i]
        elif numbers[i] > max_value:
            max_index = i
            max_value = numbers[i]
    # We will return the min and max
    return (numbers[min_index], numbers[max_index])
