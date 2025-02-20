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

    if k == 0:
        return 0

    # First, we'll sort the array
    arr.sort()
    # Next, we'll create a second list to store the
    # elements we're going to count
    second = []
    # Next, we'll count the elements
    for i in range(k):
        # Add the first element to our list
        second.append(arr[i])
    # We'll keep a counter to keep track of how many elements
    # we've counted
    count = 1
    # Now, we'll loop over the rest of the elements in our
    # original array
    for i in range(k, len(arr)):
        # If our current element is within our range of
        # the first k elements, then we'll add it to our
        # second list
        if abs(arr[i]) < 100:
            second.append(arr[i])
        # Otherwise, we'll increment our counter
        else:
            count += 1
    # Finally, we'll add the elements of our second list
    # together, and return the sum
    return sum(second) + count
