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

    def sort_at_index(l: List[int], i: int) -> List[int]:
        """Sort the list at index i
        >>> sort_at_index([1, 2, 3], 2)
        [1, 2, 3]
        >>> sort_at_index([1, 2, 3, 4], 3)
        [1, 2, 3, 4]
        >>> sort_at_index([1, 2, 3, 4, 5], 3)
        [1, 2, 3, 4, 5]
        >>> sort_at_index([1, 2, 3, 4, 5, 6], 3)
        [1, 2, 3, 4, 5, 6]
        """
        if i >= len(l): return l
        return l[:i] + sorted(l[i:])

    def get_sorted_indices(l: List[int]) -> List[int]:
        """Return a list of the indicies that are divisible by three
        >>> get_sorted_indices([1, 2, 3])
        [2]
        >>> get_sorted_indices([1, 2, 3, 4])
        [2, 4]
        >>> get_sorted_indices([1, 2, 3, 4, 5])
        [2, 4]
        >>> get_sorted_indices([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
        """
        return [i for i in range(len(l)) if i % 3 == 2]

    sorted_indices = get_sorted_indices(l)
    for i in sorted_indices:
        l = sort_at_index(l, i)

    return l
