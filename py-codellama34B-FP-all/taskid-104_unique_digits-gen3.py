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

    def has_even(n: int) -> bool:
        # return any(int(d) % 2 == 0 for d in str(n))
        while n:
            if n % 10 % 2 == 0:
                return True
            n //= 10
        return False
    return sorted(filter(lambda n: not has_even(n), x))
