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

    even_digits = []
    for i in range(10):
        if i % 2 == 0:
            even_digits.append(str(i))
    result = []
    for i in x:
        str_i = str(i)
        if all(d not in str_i for d in even_digits):
            result.append(i)
    result.sort()
    return result
