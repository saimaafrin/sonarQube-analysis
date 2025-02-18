from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    out = []
    if len(numbers) > 1:
        for i in range(len(numbers) - 1):
            out.extend([numbers[i], delimeter])
        out.append(numbers[-1])
    elif numbers:
        out.append(numbers[0])
    return out
