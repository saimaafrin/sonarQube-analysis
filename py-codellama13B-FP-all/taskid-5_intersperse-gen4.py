from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    result = []
    length = len(numbers)
    if length < 2:
        return numbers

    for i in range(0, length - 1):
        result.append(numbers[i])
        result.append(delimeter)

    result.append(numbers[length - 1])

    return result
