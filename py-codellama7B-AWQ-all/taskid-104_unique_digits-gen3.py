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
    unique_elements = []

    for number in x:
        if not any(digit % 2 == 0 for digit in str(number)):
            unique_elements.append(number)

    return sorted(unique_elements)
