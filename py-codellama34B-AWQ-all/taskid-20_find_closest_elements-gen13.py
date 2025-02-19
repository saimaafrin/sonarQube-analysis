from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """


    closest_pair: Tuple[float, float] = (0, 0)

    for index, number in enumerate(numbers):
        if index < len(numbers) - 1:
            if abs(numbers[index] - numbers[index + 1]) < abs(numbers[closest_pair[0]] - numbers[closest_pair[1]]):
                closest_pair = (index, index + 1)

    return (numbers[closest_pair[0]], numbers[closest_pair[1]])
