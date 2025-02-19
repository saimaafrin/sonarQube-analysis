from typing import List

def unique_digits(x: List[int]) -> List[int]:
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    # Your code here
    # Steps:
    #   - Iterate over the input list
    #   - For each element:
    #       - Iterate over its digits
    #       - If any digit is even, break the loop
    #       - If the loop finishes, it means no even digit was found, so add the
    #         number to the result list
    #   - Return the sorted result list
    pass
