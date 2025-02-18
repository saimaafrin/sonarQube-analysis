from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    interspersed_list = []

    # Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    for i in range(len(numbers)):
        interspersed_list.append(numbers[i])

        if i < len(numbers) - 1:
            interspersed_list.append(delimeter)

    return interspersed_list
