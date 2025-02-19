from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    >>> next_smallest([1, 2, 3, 4, 5])
    2
    >>> next_smallest([5, 1, 4, 3, 2])
    2
    >>> next_smallest([])
    None
    >>> next_smallest([1, 1])
    None
    """

    # sorted_lst = sorted(lst)
    # if len(sorted_lst) > 1:
    #     return sorted_lst[1]
    # else:
    #     return None

    # if len(lst) == 0:
    #     return None
    # elif len(lst) == 1:
    #     return None
    # else:
    #     sorted_lst = sorted(lst)
    #     return sorted_lst[1]

    # if len(lst) == 0:
    #     return None
    # elif len(lst) == 1:
    #     return None
    # else:
    #     return sorted(lst)[1]

    # if len(lst) < 2:
    #     return None
    # lst = sorted(lst)
    # return lst[1]

    if len(lst) < 2:
        return None
    return sorted(lst)[1]
