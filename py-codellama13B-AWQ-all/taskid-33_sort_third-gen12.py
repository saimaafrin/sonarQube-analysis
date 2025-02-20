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

    # sort l's values at indicies that are divisible by three
    l_prime = [i for i in l]
    for i in range(len(l_prime)):
        if i % 3 == 0:
            l_prime[i] = sorted(l_prime[i])
    # return l'
    return l_prime
