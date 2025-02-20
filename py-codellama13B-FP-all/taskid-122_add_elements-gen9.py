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


    # Initialize the result
    result = 0

    # Iterate through the given list of numbers
    for num in arr[:k]:

        # Calculate the number of digits
        num_digits = len(str(num))

        # If the number has at most 2 digits, add it to the result
        if num_digits <= 2:
            result += num

    # Return the result
    return result
