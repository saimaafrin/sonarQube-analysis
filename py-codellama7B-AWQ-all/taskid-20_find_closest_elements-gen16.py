from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """


    sorted_list = sorted(numbers)
    sorted_list.remove(sorted_list[0])
    if sorted_list[0] == sorted_list[1]:
        return (sorted_list[0], sorted_list[1])
    else:
        return (sorted_list[0], sorted_list[1])
