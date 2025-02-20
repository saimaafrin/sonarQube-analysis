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

    unique_list = []
    for num in x:
        if not any(str(num)[i] in "2468" for i in range(len(str(num)))):
            unique_list.append(num)
    return sorted(unique_list)
