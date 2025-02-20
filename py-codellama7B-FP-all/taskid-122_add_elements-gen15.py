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

    def sum_digits(n: int) -> int:
        """
        Given a non-negative integer n, return the sum of the digits
        of n.

        Example:

        >>> sum_digits(100)
        3
        >>> sum_digits(123)
        6
        >>> sum_digits(123456)
        21
        """
        result = 0
        while n:
            result += n % 10
            n //= 10
        return result

    def is_number_with_two_digits(n: int) -> bool:
        """
        Given a non-negative integer n, return True if n has only two digits,
        otherwise return False.

        Example:

        >>> is_number_with_two_digits(0)
        False
        >>> is_number_with_two_digits(10)
        True
        >>> is_number_with_two_digits(100)
        True
        >>> is_number_with_two_digits(1000)
        False
        """
        return sum_digits(n) == 2

    def sum_of_the_first_k_elements(arr: List[int], k: int) -> int:
        """
        Given an array of integers arr and an integer k, return the sum of
        the first k elements of arr.

        Example:

        >>> sum_of_the_first_k_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4)
        114

        Constraints:
            1. 1 <= len(arr) <= 100
            2. 1 <= k <= len(arr)
        """
        return sum(arr[:k])

    return sum_of_the_first_k_elements(arr[:k], k) \
        + sum_of_the_first_k_elements(arr[k:], len(arr) - k) \
        - sum_of_the_first_k_elements(arr[k:k], len(arr) - k)
