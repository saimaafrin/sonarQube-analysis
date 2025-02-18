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

    # Your code here
    def check_for_even_digits(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if int(str_num[i]) % 2 == 0:
                return True
        return False
    
    x_ = []
    for i in x:
        if not check_for_even_digits(i):
            x_.append(i)
    x_.sort()
    return x_
