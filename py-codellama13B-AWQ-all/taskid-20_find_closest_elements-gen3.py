from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # For a list of at least two elements, we can always find the two closest to each other.
    # We can start by sorting the list and then looking at the differences between adjacent elements.
    numbers.sort()
    closest_pair_difference = numbers[1] - numbers[0]
    closest_pair_indices = (0, 1)
    for i in range(len(numbers) - 1):
        # Look at the differences between adjacent elements.
        difference = numbers[i+1] - numbers[i]
        if difference < closest_pair_difference:
            # If we find an element with a smaller difference, then update the closest pair.
            closest_pair_difference = difference
            closest_pair_indices = (i, i+1)
    return (numbers[closest_pair_indices[0]], numbers[closest_pair_indices[1]])
