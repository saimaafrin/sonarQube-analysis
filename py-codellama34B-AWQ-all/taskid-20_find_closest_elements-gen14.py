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
        raise ValueError("You need at least two numbers to find the closest pair!")
    elif len(numbers) == 2:
        return (numbers[0], numbers[1])

    numbers.sort()

    closest_pair = (numbers[0], numbers[1])
    closest_distance = abs(numbers[0] - numbers[1])

    for i in range(0, len(numbers) - 1):
        distance = abs(numbers[i] - numbers[i + 1])
        if distance < closest_distance:
            closest_distance = distance
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair
