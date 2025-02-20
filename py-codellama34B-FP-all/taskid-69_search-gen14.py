from typing import List

def search(lst: List[int]) -> int:
    """
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
    >>> search([4, 1, 2, 2, 3, 1])
    2
    >>> search([1, 2, 2, 3, 3, 3, 4, 4, 4])
    3
    >>> search([5, 5, 4, 4, 4])
    -1
    """

    # my solution
    # step1: store the unique element in list and record its freq
    # step2: filter out element whose freq < element
    # step3: max
    if not lst:
        return -1
    unique_lst = set(lst)
    frequency_dic = {}
    for e in unique_lst:
        frequency_dic[e] = lst.count(e)
    unique_lst = list(filter(lambda x: frequency_dic[x] >= x, unique_lst))
    if not unique_lst:
        return -1
    return max(unique_lst)
