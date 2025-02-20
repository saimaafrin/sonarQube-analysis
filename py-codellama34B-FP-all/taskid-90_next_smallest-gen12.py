from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    >>> next_smallest([1, 2, 3, 4, 5])
    2
    >>> next_smallest([5, 1, 4, 3, 2])
    2
    >>> next_smallest([])
    None
    >>> next_smallest([1, 1])
    None
    """

    # Check if the list is empty or not
    if not lst:
        return None
    else:
        # Get the smallest number in the list
        smallest = min(lst)
        # Get the index of the smallest number in the list
        smallest_index = lst.index(smallest)
        # Remove the smallest number from the list
        lst.pop(smallest_index)
        # Get the smallest number from the new list
        new_smallest = min(lst)
        # Get the index of the smallest number in the new list
        new_smallest_index = lst.index(new_smallest)
        # Remove the smallest number from the new list
        lst.pop(new_smallest_index)
        # Return the smallest number from the new list
        return new_smallest
