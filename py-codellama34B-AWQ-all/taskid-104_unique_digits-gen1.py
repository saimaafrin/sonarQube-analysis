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

    def check(x: int) -> bool:
        """Returns True if x has no even digit, False otherwise."""
        return not any(int(digit) % 2 == 0 for digit in str(x))

    return sorted([num for num in x if check(num)])
