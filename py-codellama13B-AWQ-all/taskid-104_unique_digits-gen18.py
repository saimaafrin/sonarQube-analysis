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
        temp = []
        temp2 = list(str(i))
        for j in temp2:
            if int(j) % 2 == 0:
                break
            else:
                temp.append(j)
        if temp == temp2:
            res.append(i)
    return sorted(res)
