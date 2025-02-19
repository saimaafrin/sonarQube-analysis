from typing import List

def solution(lst: List[int]) -> int:
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    >>> solution([5, 8, 7, 1])
    12
    >>> solution([3, 3, 3, 3, 3])
    9
    >>> solution([30, 13, 24, 321])
    0
    """


    # lst.index() returns the index of the first occurrence
    # of the value in the list
    # e.g. lst.index(8) will return 1
    # even_index_values = [lst[lst.index(elem)] for elem in lst if lst.index(elem) % 2 == 0]

    even_index_values = []

    for i, num in enumerate(lst):
        if i % 2 == 0:
            even_index_values.append(num)

    return sum(even_index_values)
