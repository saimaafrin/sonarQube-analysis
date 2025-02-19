from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # Create an empty list to store the unique items
    unique: List[int] = []

    # Iterate through the input list
    for item in numbers:
        # If the item is not in the unique list...
        if item not in unique:
            # ... add it to the unique list
            unique.append(item)

    return unique
