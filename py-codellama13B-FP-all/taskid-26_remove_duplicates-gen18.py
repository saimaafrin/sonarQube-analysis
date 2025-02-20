from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # Set of unique numbers, order of elements is preserved
    unique = set()
    # List of unique numbers
    unique_list = []
    # Go through the list of integers
    for num in numbers:
        # If the number is not already in the set
        if num not in unique:
            # Add it to the set
            unique.add(num)
            # Add it to the list
            unique_list.append(num)
    return unique_list
