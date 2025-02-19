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
    if len(numbers) == 2:
        return (numbers[0], numbers[1])
    closest_pair = []
    for i, number in enumerate(numbers):
        if i == len(numbers) - 1:
            closest_pair.append(number)
            break
        if numbers[i + 1] - number < number - numbers[i - 1]:
            closest_pair = [number, numbers[i + 1]]
    return tuple(closest_pair)
