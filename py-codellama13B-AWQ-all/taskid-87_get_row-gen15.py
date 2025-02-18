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


    # create an empty list to store coordinates
    coordinates: List[Tuple[int, int]] = []

    for y, row in enumerate(lst):
        # loop through each row
        if x in row:
            # if x is present in the row, add a coordinate
            # to the coordinates list.
            # coordinates.append((y, row.index(x)))
            coordinates.append((y, len(row) - 1 - row[::-1].index(x)))

    # sort the coordinates by row in ascending order
    # and sort coordinates of the same row by columns in descending order
    return sorted(coordinates, key=lambda x: (x[0], -x[1]))
