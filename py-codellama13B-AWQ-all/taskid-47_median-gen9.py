from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    # Sort a copy of l, then take the middle element.
    ll = sorted(l)
    if len(ll) % 2 == 0:
        # If we have an even number of elements, take the mean of the 2 elements in the middle.
        median_index = len(ll) // 2
        return (ll[median_index - 1] + ll[median_index]) / 2
    else:
        # If we have an odd number of elements, take the middle element.
        median_index = (len(ll) - 1) // 2
        return ll[median_index]
