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
        raise ValueError("List must have at least 2 numbers.")

    closest_elements = []
    closest_difference = None

    for i in range(len(numbers)-1):
        difference = numbers[i+1] - numbers[i]
        if closest_difference is None or difference < closest_difference:
            closest_difference = difference
            closest_elements = [numbers[i], numbers[i+1]]

    return (min(closest_elements), max(closest_elements))
