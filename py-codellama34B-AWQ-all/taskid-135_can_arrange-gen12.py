from typing import List

def can_arrange(arr: List[int]) -> int:
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    >>> can_arrange([1, 2, 4, 3, 5])
    3
    >>> can_arrange([1, 2, 3])
    -1
    """

    if not arr:
        return -1
    stack = []
    for i, element in enumerate(arr):
        if not stack or stack[-1] < element:
            stack.append(i)
        else:
            j = len(stack) - 1
            while stack and stack[j] >= element:
                j -= 1
            stack[j + 1:] = []
            stack.append(i)
    return stack[-1]
