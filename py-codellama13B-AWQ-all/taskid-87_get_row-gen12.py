from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    >>> get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1)
    [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    >>> get_row([], 1)
    []
    >>> get_row([[], [1], [1, 2, 3]], 3)
    [(2, 2)]
    """

    result: List[Tuple[int, int]] = []
    for i, row in enumerate(lst):
        if x in row:
            result.append((i, row.index(x)))
    result.sort(key=lambda x: (x[0], len(lst[x[0]])))
    for i, e in enumerate(result):
        if i > 0 and result[i - 1][0] == e[0]:
            result[i - 1] = (e[0], len(lst[e[0]]) - 1 - e[1])
    return result
