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

    # Create dictionary with index of integer as key and count of integer as value
    freqs = {}
    for i, n in enumerate(lst):
        if n not in freqs:
            freqs[n] = 0
        freqs[n] += 1
    
    # Sort dictionary by key
    sorted_freqs = list(sorted(freqs.items()))

    # Iterate over sorted dictionary to find largest integer
    # that is greater than zero and has frequency greater than or equal to the value of the integer itself
    for k, v in sorted_freqs:
        if k > 0 and v >= k:
            return k

    return -1
