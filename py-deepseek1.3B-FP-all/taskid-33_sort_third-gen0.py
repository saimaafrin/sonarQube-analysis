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

    # Your solution here
    divisible_by_three = [l[i] for i in range(len(l)) if (i+1) % 3 == 0]
    divisible_by_three.sort()

    result = []
    j = 0
    for i in range(len(l)):
        if (i+1) % 3 == 0:
            result.append(divisible_by_three[j])
            j += 1
        else:
            result.append(l[i])

    return result
