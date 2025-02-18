from typing import List

def will_it_fly(q: List[int], w: int) -> bool:
    """
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    >>> will_it_fly([1, 2], 5)
    False
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    >>> will_it_fly([3, 2, 3], 1)
    False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    >>> will_it_fly([3, 2, 3], 9)
    True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    >>> will_it_fly([3], 5)
    True
    # 3 is less than the maximum possible weight, and it's balanced.
    """


    if len(q) == 1:
        return w >= q[0]

    def sum_of_all_subarrays(a: List[int]) -> int:
        """
        Write a function that takes in an array of integers and returns the sum of all possible subarrays.

        Example:
        >>> sum_of_all_subarrays([1, 2, 3])
        15

        # All possible subarrays are:
        # [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]

        >>> sum_of_all_subarrays([1, 2, 3, 4])
        40

        # All possible subarrays are:
        # [1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]

        >>> sum_of_all_subarrays([1, 2, 3, 4, 5])
        90

        # All possible subarrays are:
        # [1], [2], [3], [4], [5], [1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5], [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5], [1, 2, 3, 4, 5]

        >>> sum_of_all_subarrays([1, 2, 3, 4, 5, 6])
        210

        # All possible subarrays are:
        # [1], [2], [3], [4], [5], [6], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 3], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6], [4, 5], [4, 6], [5, 6], [1, 2, 3], [1, 2, 4
