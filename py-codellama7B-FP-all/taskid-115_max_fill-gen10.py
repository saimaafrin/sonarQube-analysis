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


    # 1. Find the largest column with a 1 in it.
    # 2. Fill that column with the buckets.
    # 3. If any other columns have a 1 in them, move the buckets down to that column and start filling again.
    # 4. If the largest column has all 1s, return the number of times you need to move the buckets.

    # 1. find the largest column
    columns = [[] for _ in range(len(grid[0]))]
    for row in grid:
        for i, col in enumerate(row):
            if col == 1:
                columns[i].append(row)
    
    largest_column = max(columns, key=len)
    largest_column_index = columns.index(largest_column)
    bucket_count = len(largest_column)

    # 2. fill the column with the buckets
    for row in largest_column:
        row[largest_column_index] = 0

    # 3. if any other columns have a 1 in them, move the buckets down to that column and start filling again.
    while bucket_count < capacity:
        # 4. If the largest column has all 1s, return the number of times you need to move the buckets.
        if not largest_column:
            return bucket_count

        largest_column = columns[largest_column_index]
        bucket_count = len(largest_column)

        for i, row in enumerate(largest_column):
            row[largest_column_index] = 0

        columns[largest_column_index] = largest_column[i+1:]

        if columns[largest_column_index]:
            largest_column = columns[largest_column_index]

        largest_column_index += 1

    return bucket_count
