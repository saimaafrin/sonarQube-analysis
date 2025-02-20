from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Check if there are at least two elements in the list.
    if len(numbers) < 2:
        raise ValueError("Expected two or more elements in the list, got {0}.".format(len(numbers)))

    # Store the smallest difference between two elements in the list.
    min_diff = float("inf")

    # Store the two elements that have the smallest difference between them.
    num_1 = num_2 = None

    # Go through all pairs of elements in the list.
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            # Find the absolute difference between the two elements.
            diff = abs(numbers[i] - numbers[j])

            # If the difference is the smallest we've seen so far, store the two elements.
            if diff < min_diff:
                min_diff = diff
                num_1 = numbers[i]
                num_2 = numbers[j]

    # Return the two elements in order (smaller number, larger number).
    return (num_1, num_2)
