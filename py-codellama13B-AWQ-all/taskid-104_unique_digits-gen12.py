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


    # sort list
    x.sort()

    # filter list
    new_list = []
    for num in x:
        has_even_digit = False
        while num > 0:
            if num % 10 == 0:
                break
            elif num % 2 == 0:
                has_even_digit = True
                break
            else:
                num = num // 10
        if not has_even_digit:
            new_list.append(num)
    
    return new_list
