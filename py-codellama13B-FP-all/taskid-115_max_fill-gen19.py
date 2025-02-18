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


    # initialize answer
    answer = 0

    # set grid length and capacity
    grid_length = len(grid)
    capacity = capacity

    # create a list for the current capacity
    current_capacity = [0] * grid_length

    # loop until the buckets are empty
    while True:

        # check if the capacity is greater than the current capacity
        if capacity > sum(current_capacity):

            # increment the answer
            answer += 1

            # fill the current capacity with the capacity
            for i in range(grid_length):
                current_capacity[i] += capacity - sum(current_capacity)

        # if the capacity is less than the current capacity
        else:

            # decrement the answer
            answer -= 1

            # remove capacity from the current capacity
            for i in range(grid_length):
                current_capacity[i] -= capacity

        # check if the buckets are empty
        if sum(current_capacity) == 0:

            # return the answer
            return answer

        # if the buckets are not empty
        else:

            # update the capacity
            capacity = sum(current_capacity)
