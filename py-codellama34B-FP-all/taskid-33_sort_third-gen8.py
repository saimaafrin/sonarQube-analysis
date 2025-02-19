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

    if len(l) == 1:
        return l
    first_half = sort_third(l[0:len(l)//2])
    second_half = sort_third(l[len(l)//2:])
    i, j = 0, 0
    result = []
    while len(result) < len(l):
        if i < len(first_half) and j == len(second_half):
            result.append(first_half[i])
            i += 1
        elif i == len(first_half) and j < len(second_half):
            result.append(second_half[j])
            j += 1
        elif i < len(first_half) and j < len(second_half):
            if (len(result) + 1) % 3 == 0:
                result.append(min(first_half[i], second_half[j]))
                if first_half[i] <= second_half[j]:
                    i += 1
                else:
                    j += 1
            else:
                result.append(first_half[i])
                i += 1
                result.append(second_half[j])
                j += 1
    return result
