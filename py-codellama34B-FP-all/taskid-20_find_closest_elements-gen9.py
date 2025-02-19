from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Sort the input list
    numbers.sort()
    # Initialize the difference between the smallest two elements as the first element
    difference = numbers[0]
    # Initialize the indices of the smallest two elements as 0 and 1
    closest_indices = (0, 1)
    # Loop over the list
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current and next elements
        current_difference = numbers[i + 1] - numbers[i]
        # Check if the current difference is smaller than the smallest difference
        if current_difference < difference:
            # If the current difference is smaller, update the smallest difference
            difference = current_difference
            # Update the indices of the smallest two elements
            closest_indices = (i, i + 1)
    # Return the smallest two elements
    return (numbers[closest_indices[0]], numbers[closest_indices[1]])
