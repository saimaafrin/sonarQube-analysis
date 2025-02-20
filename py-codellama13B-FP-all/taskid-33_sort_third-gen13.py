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


    result = []
    length = len(l)
    for i in range(length):
        if i % 3 == 0:
            result.append(l[i])
        elif i % 3 == 1:
            if l[i] < result[i - 1]:
                result.append(result[i - 1])
            else:
                result.append(l[i])
        else:
            if l[i] < result[i - 2]:
                result.append(result[i - 2])
            else:
                result.append(l[i])
    return result
