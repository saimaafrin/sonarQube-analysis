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

    # 1. Store all the indices that are divisible by three in a list
    # 2. Store all the indicies that are not divisible by three in a list
    # 3. Sort the list of indicies that are divisible by three
    # 4. Use the sorted list to find the indices that need to be swapped
    # 5. Swap the values at those indices
    pass
    return l
