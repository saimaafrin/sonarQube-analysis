from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    num_list = []
    for num in numbers:
        if num_list == []:
            num_list.append(num)
        else:
            if num_list[-1] >= num:
                num_list.append(num)
            else:
                num_list.insert(0, num)
    return tuple(num_list[1:])
