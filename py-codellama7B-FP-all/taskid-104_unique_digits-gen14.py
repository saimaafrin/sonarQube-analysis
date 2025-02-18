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

    # Your Code Here
    def is_even(n: int) -> bool:
        return n % 2 == 0

    def is_odd(n: int) -> bool:
        return n % 2 != 0

    return [x for x in x if all(map(is_odd, str(x)))]
