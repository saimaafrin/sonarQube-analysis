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

    result = []
    for i in range(len(lst)):
        row = lst[i]
        for j in range(len(row)):
            if row[j] == x:
                result.append((i, j))
    result.sort()
    for i in range(len(result)):
        if result[i][0] == result[i-1][0]:
            result[i].append(result[i-1][1])
            result[i-1].append(result[i][1])
            result[i-1].pop()
            result[i].pop()
    result.sort(key = lambda x: x[1], reverse=True)
    return result
