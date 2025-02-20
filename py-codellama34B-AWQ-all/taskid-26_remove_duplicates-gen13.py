from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # sort the list for the below algorithm to work
    numbers.sort()
    uniques = []
    for i, x in enumerate(numbers):
        # if the current element has not been seen before,
        # or it has been seen only once (and so is itself a unique),
        # add it to the result
        if x not in numbers[:i] or x in numbers[:i] and numbers.count(x) == 1:
            uniques.append(x)
    return uniques
