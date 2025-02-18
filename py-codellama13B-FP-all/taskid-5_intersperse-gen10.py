from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    if len(numbers) < 2:
        return numbers
    result = []
    i = 0
    while i < len(numbers):
        result.append(numbers[i])
        if i + 1 < len(numbers):
            result.append(delimeter)
        i += 1
    return result
