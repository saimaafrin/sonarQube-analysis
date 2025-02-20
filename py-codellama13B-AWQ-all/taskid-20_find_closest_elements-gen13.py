from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    assert len(numbers) >= 2
    distance = abs(numbers[0] - numbers[1])
    best = (numbers[0], numbers[1])
    for idx in range(len(numbers)-1):
        for inner_idx in range(idx+1, len(numbers)):
            new_distance = abs(numbers[idx] - numbers[inner_idx])
            if new_distance < distance:
                distance = new_distance
                best = (numbers[idx], numbers[inner_idx])
    return best
