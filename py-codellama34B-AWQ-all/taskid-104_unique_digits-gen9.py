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


    has_even = False
    x.sort()
    for i in x:
        while i:
            if i%2 == 0:
                has_even = True
                break
            i = i//10
        if has_even:
            has_even = False
            x.remove(i)
    
    return x
