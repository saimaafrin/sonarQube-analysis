from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Sort the list in ascending order
    numbers.sort()

    # Set the first two values as the closest to each other
    closest_numbers = (numbers[0], numbers[1])

    # For each index of the list
    for index in range(2, len(numbers)):
        # Get the current number and the difference between the current number and the current closest numbers
        current_number = numbers[index]
        current_difference = abs(current_number - closest_numbers[0])

        # If the current difference is less than the current closest difference
        if current_difference < abs(closest_numbers[1] - closest_numbers[0]):
            # Update the closest numbers
            closest_numbers = (current_number, closest_numbers[1])

        # If the current difference is equal to the current closest difference
        elif current_difference == abs(closest_numbers[1] - closest_numbers[0]):
            # Update the closest numbers
            closest_numbers = (closest_numbers[0], current_number)

    # Return the closest numbers
    return closest_numbers
