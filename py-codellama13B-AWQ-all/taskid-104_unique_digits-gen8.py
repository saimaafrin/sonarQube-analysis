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

    return sorted(set(x) - set(i for i in x if '0' in str(i) or '2' in str(i) or '4' in str(i) or '6' in str(i) or '8' in str(i)))
