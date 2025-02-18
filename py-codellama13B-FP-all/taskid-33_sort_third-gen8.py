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

    length = len(l)
    # initialize a list to hold values not divisible by three
    # initialize a list to hold values divisible by three
    divisible = []
    not_divisible = []

    # fill in the lists based on divisibility by three
    for i in range(length):
        if i % 3 == 0:
            divisible.append(l[i])
        else:
            not_divisible.append(l[i])
    
    # sort the divisible list
    divisible.sort()
    
    # create a list to hold the sorted list
    sorted_list = []

    # add the sorted divisible list to the not divisible list
    for i in range(length):
        if i % 3 == 0:
            sorted_list.append(divisible[i // 3])
        else:
            sorted_list.append(not_divisible[i])
    return sorted_list
