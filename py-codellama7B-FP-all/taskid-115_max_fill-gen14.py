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


    # The maximum number of times you need to lower the buckets.
    result = 0
    # The index of the well that has not been filled.
    index_of_well = -1
    # The maximum height of the bucket.
    max_height = 0
    # The number of times you need to lower the bucket.
    count = 0

    # If the well has not been filled.
    while index_of_well < 0:
        # Find the next well that has not been filled.
        while index_of_well < 0 and count < grid.length:
            for i in range(count, grid.length):
                # If the well has not been filled.
                if not grid[i][count]:
                    index_of_well = i
                    break
            count += 1

        # If there is no well that has not been filled.
        if index_of_well < 0:
            break

        # The height of the bucket.
        height = grid[index_of_well][count]
        # If the height of the bucket is less than the maximum height.
        if height < max_height:
            # The number of times you need to lower the bucket.
            result += max_height - height

        # The maximum height of the bucket.
        max_height = max(max_height, height)
        # The well has been filled.
        grid[index_of_well][count] = 0
        # The well has not been filled.
        index_of_well = -1
        # The number of times you need to lower the bucket.
        count = 0

    return result
