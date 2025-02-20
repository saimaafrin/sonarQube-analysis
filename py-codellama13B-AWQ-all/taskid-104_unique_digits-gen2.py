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

    res = []
    for i in x:
        even = False
        for d in str(i):
            if int(d) % 2 == 0:
                even = True
                break
        if not even:
            res.append(i)
    res.sort()
    return res
