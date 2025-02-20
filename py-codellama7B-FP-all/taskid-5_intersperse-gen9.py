from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    # Note: for some inputs, the code below will not work
    # (e.g. when input list is empty)
    # This is because in Python, we can't append to a list
    # while iterating over that same list.
    # To avoid this problem, we create a new list,
    # and then return that.
    result = []
    for i, x in enumerate(numbers):
        if i != len(numbers) - 1:
            result.append(x)
            result.append(delimeter)
    result.append(numbers[-1])
    return result
\end{code}
