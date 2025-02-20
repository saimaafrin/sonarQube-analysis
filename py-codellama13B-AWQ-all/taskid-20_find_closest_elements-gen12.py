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
        raise ValueError("You must supply at least two numbers")

    sorted_list = sorted(numbers)
    closest = sorted_list[0]
    closest_pair = (closest, closest)

    for i in range(1, len(sorted_list)):
        if abs(sorted_list[i] - closest) < abs(closest_pair[1] - closest_pair[0]):
            closest_pair = (closest, sorted_list[i])

    return closest_pair
