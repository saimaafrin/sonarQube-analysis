from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    assert len(numbers) >= 2, "Must supply at least two numbers"
    minimum_distance = abs(numbers[0] - numbers[1])
    closest_pair = (numbers[0], numbers[1])
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if distance < minimum_distance:
                minimum_distance = distance
                closest_pair = (numbers[i], numbers[j])
    return sorted(closest_pair)
