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


    # 1. Sort the list in ascending order
    arr.sort()

    # 2. Iterate through each element
    for i in range(1, len(arr)):

        # 3. If the current element is greater than the previous element
        if arr[i] >= arr[i-1]:
            # 4. Swap the two elements
            arr[i], arr[i-1] = arr[i-1], arr[i]

            # 5. If the swapped element is not the first element
            if i-1 > 0:
                # 6. If the previous element is less than the previous
                #    element, then return the index of the swapped element
                if arr[i-1] < arr[i-2]:
                    return i

    # 7. If no swap occurred, then return -1
    return -1
