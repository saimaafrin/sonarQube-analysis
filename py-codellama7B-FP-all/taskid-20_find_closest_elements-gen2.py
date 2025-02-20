from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    smallest = 0
    largest = 0
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if abs(numbers[j] - numbers[i]) < abs(numbers[largest] - numbers[smallest]):
                smallest = i
                largest = j

    return numbers[smallest], numbers[largest]
