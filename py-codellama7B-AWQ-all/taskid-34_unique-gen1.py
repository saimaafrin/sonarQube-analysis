from typing import List

def unique(l: List[int]) -> List[int]:
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    # the trick to avoid O(n^2) algo is to use a set
    # this can not be used for duplicate strings or any other
    # complex objects
    return sorted(set(l))
\end{code}
