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
        raise ValueError("Must supply at least two numbers")

    # sort numbers
    numbers.sort()

    # find the two smallest values that are the closest
    closest_distance = float('inf')
    for i in range(len(numbers) - 1):
        distance = numbers[i + 1] - numbers[i]
        if distance < closest_distance:
            closest_distance = distance
            closest_pair = (numbers[i], numbers[i + 1])

    # return the pair
    return closest_pair
