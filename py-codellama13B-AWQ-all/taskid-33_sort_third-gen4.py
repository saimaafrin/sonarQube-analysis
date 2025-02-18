from typing import List

def sort_third(l: List[int]) -> List[int]:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """


    # list to store elements that need to be sorted
    sorted_indices = []

    # list to store elements that don't need to be sorted
    unsorted_indices = []

    for i in range(len(l)):
        # check if the index is divisible by three
        if i % 3 == 0:
            # add to sorted indices
            sorted_indices.append(l[i])
        else:
            # add to unsorted indices
            unsorted_indices.append(l[i])

    # sort the sorted indices
    sorted_indices.sort()

    # iterate through both lists and copy elements from the sorted list into the new list
    # unsorted indices are added first
    result = []
    for i in range(len(unsorted_indices)):
        result.append(unsorted_indices[i])

    # append sorted elements to the result list
    for i in range(len(sorted_indices)):
        result.append(sorted_indices[i])

    return result
