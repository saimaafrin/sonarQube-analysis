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


    def freq(x: int) -> int:
        return lst.count(x)

    def find_max(x: int) -> int:
        """Return the greatest integer that is greater than 0 and has a frequency greater than or equal 
        to the value of the integer itself.
        """
        if x == 0:
            return -1
        for i in range(x, max(lst) + 1):
            if freq(i) >= x:
                return i
        return -1

    return max(map(find_max, lst))
