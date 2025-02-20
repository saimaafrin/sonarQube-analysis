from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Sort the input numbers list from smallest to largest
    sorted_numbers = sorted(numbers)
    # Assign smallest value in the list to the first variable
    first = sorted_numbers[0]
    # Assign largest value in the list to the second variable
    second = sorted_numbers[-1]
    # Loop through the input list
    for index, element in enumerate(sorted_numbers):
        # If the current index plus one is less than the length of the list
        if index + 1 < len(sorted_numbers):
            # Assign the next element to the third variable
            third = sorted_numbers[index + 1]
            # If the difference between the current element and the next element is less than the difference between
            # the first and second variables
            if abs(element - third) < abs(first - second):
                # Assign the current element to the first variable
                first = element
                # Assign the next element to the second variable
                second = third
    return (first, second)
