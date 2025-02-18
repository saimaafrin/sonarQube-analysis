from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    # Sort the list.
    l.sort()
    # Find the median.
    if len(l) % 2 == 1:
        # Odd number of elements.
        return l[len(l) // 2]
    # Even number of elements.
    return (l[len(l) // 2] + l[(len(l) // 2) - 1]) / 2
\end{code}
