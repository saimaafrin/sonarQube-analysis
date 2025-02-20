from typing import List

def sort_even(l: List[int]) -> List[int]:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    even_indexes = [i for i in range(len(l)) if i % 2 == 0]
    l_prime = [l[i] for i in range(len(l)) if i not in even_indexes]
    for i in range(len(even_indexes)):
        l_prime.insert(even_indexes[i], l[even_indexes[i]])
    l_prime.extend(sorted(l[i] for i in even_indexes))
    return l_prime
