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


    # max_value_freq = -1
    # max_value = -1
    # for value in lst:
    #     freq = lst.count(value)
    #     if freq > max_value_freq:
    #         max_value_freq = freq
    #         max_value = value
    #     elif freq == max_value_freq:
    #         if value > max_value:
    #             max_value = value

    # if max_value_freq > 0 and max_value_freq >= max_value:
    #     return max_value
    # else:
    #     return -1

    # Pythonic
    count = {i: lst.count(i) for i in set(lst)}
    return max(x for x, y in count.items() if y >= x) if count else -1
