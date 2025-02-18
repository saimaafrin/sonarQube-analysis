from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
    >>> max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1)
    6

    Example 2:
    >>> max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2)
    5
    
    Example 3:
    >>> max_fill([[0, 0, 0], [0, 0, 0]], 5)
    0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """


    def get_row_index_with_max_capacity(grid: List[List[int]], row_index: int) -> int:
        max_capacity_row_index = -1
        for row in grid:
            if row_index == 0:
                max_capacity_row_index = 0
            if row_index > 0 and row[row_index] > row[max_capacity_row_index]:
                max_capacity_row_index = row_index
        return max_capacity_row_index

    def get_row_index_with_max_value(grid: List[List[int]], row_index: int) -> int:
        max_value_row_index = -1
        for row in grid:
            if row_index == 0:
                max_value_row_index = 0
            if row_index > 0 and row[row_index] > row[max_value_row_index]:
                max_value_row_index = row_index
        return max_value_row_index

    def get_column_index_with_max_value(grid: List[List[int]], row_index: int) -> int:
        max_value_column_index = -1
        for column_index in range(len(grid[row_index])):
            if column_index == 0:
                max_value_column_index = 0
            if column_index > 0 and grid[row_index][column_index] > grid[row_index][max_value_column_index]:
                max_value_column_index = column_index
        return max_value_column_index

    def get_max_value(grid: List[List[int]], row_index: int, column_index: int) -> int:
        if row_index < 0 or row_index >= len(grid) or column_index < 0 or column_index >= len(grid[row_index]):
            return -1
        return grid[row_index][column_index]

    def get_min_value(grid: List[List[int]], row_index: int, column_index: int) -> int:
        if row_index < 0 or row_index >= len(grid) or column_index < 0 or column_index >= len(grid[row_index]):
            return -1
        return grid[row_index][column_index]

    def get_max_value_on_row(grid: List[List[int]], row_index: int) -> int:
        max_value_on_row = -1
        for column_index in range(len(grid[row_index])):
            if column_index == 0:
                max_value_on
