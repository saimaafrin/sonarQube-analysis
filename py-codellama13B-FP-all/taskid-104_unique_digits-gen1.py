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


    y: List[int] = []

    for i in x:
        s = str(i)
        if (len(s) > 1 and s[0] != "1") or len(s) == 1:
            y.append(i)

    return sorted(y)
