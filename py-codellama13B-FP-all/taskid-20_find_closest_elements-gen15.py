from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """


    assert len(numbers) >= 2, 'Must supply at least two numbers.'
    assert all([type(n) == float for n in numbers]), 'All numbers must be of type float.'

    diffs = [(n1, abs(n1 - n2)) for n1, n2 in zip(numbers, numbers[1:])]
    closest_diffs = min(diffs, key=lambda x: x[1])
    closest_diff = closest_diffs[1]

    closest_nums = (n for n, d in diffs if d == closest_diff)
    return tuple(sorted(closest_nums))
