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

    def is_third(i: int) -> bool:
        return i % 3 == 0
    
    def insert_sorted(mylist: List[int], element: int) -> List[int]:
        # TODO: Implement
        return []
    
    return [element for element in l if not is_third(l.index(element))] + [*insert_sorted(l[::3], *l[::3])] + [*insert_sorted(l[1::3], *l[1::3])] + [*insert_sorted(l[2::3], *l[2::3])]
