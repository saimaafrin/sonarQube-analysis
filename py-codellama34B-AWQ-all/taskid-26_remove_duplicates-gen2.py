from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # Create an empty list to store unique elements
    unique_elements = []

    # Iterate over the input list
    for number in numbers:
        # Check if the current element is already in the unique elements list
        if number not in unique_elements:
            # If not, add it to the unique elements list
            unique_elements.append(number)

    return unique_elements
