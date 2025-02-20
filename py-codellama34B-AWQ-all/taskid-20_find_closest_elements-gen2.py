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
    closest = (0, 1)
    for i in range(len(numbers)-1):
        if abs(numbers[i] - numbers[i+1]) < abs(numbers[closest[0]] - numbers[closest[1]]):
            closest = (i, i+1)
    return numbers[closest[0]], numbers[closest[1]]
