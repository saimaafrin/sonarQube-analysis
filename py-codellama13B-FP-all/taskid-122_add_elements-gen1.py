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


    # initialize variables
    count = 0
    first_two_digits = False

    # iterate over array
    for num in arr[:k]:
        # check if number is greater than or equal to 10
        if num >= 10:
            # if number is greater than or equal to 10
            if first_two_digits:
                # if number is greater than or equal to 10 and first two digits have already been found
                count += num // 10
            else:
                # if number is greater than or equal to 10 and first two digits have not been found
                count += min(num // 10, 99)

            # set flag
            first_two_digits = True

        # check if number is less than or equal to 9
        elif num <= 9:
            # if number is less than or equal to 9
            count += num

        # check if number is equal to 10
        elif num == 10:
            # if number is equal to 10
            count += num

    # return result
    return count
