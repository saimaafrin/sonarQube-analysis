from typing import List

def add_elements(arr: List[int], k: int) -> int:
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

    >>> add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4)
    24

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """

    # Time complexity: O(n)
    # Space complexity: O(1)
    # Note: This is done using a mathematical approach:
    # If the number has 2 or less digits, then it will sum the digits.
    # If the number has 3 digits, then we can find the first digit by
    # dividing the number by 100, then we sum all the digits except the first
    # digit, and then we add the first digit to the result.
    # We repeat this process for the numbers with 3 digits, until we
    # have reached the k'th element.
    # After that, we add all the elements with 2 digits.

    result = 0
    count = 0

    for element in arr:
        if count == k:
            break
        count += 1
        if element < 100:
            result += element
        else:
            result += element // 100 + (element % 100)

    for element in arr[count:]:
        if element < 100:
            result += element

    return result
