from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    if len(numbers) == 0:
        return []
    # Insert 'delimeter' in-between every two consecutive numbers
    result = [numbers[0]]
    for n in numbers[1:]:
        result.append(delimeter)
        result.append(n)
    return result
