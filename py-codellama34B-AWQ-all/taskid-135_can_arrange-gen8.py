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

    stack = []
    n = len(arr)

    for i in range(n):
        if not stack or arr[i] <= stack[-1]:
            stack.append(arr[i])
        else:
            while stack and stack[-1] < arr[i]:
                stack.pop()
            stack.append(arr[i])
    
    return len(stack) - 1
