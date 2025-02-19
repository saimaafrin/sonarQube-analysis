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

    ret = []
    for num in x:
        tmp = str(num)
        if '2' in tmp or '4' in tmp or '6' in tmp or '8' in tmp or '0' in tmp:
            continue
        else:
            ret.append(num)
    ret.sort()
    return ret
