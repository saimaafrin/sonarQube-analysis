from typing import List

def skjkasdkd(lst: List[int]) -> int:
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    >>> skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3])
    10
    >>> skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1])
    25
    >>> skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3])
    13
    >>> skjkasdkd([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6])
    11
    >>> skjkasdkd([0, 81, 12, 3, 1, 21])
    3
    >>> skjkasdkd([0, 8, 1, 2, 1, 7])
    7
    """

    # your code here
    # i = 0
    # largest_prime = 0
    # sum_of_digits = 0
    # while i < len(lst):
    #     if is_prime(lst[i]):
    #         if largest_prime < lst[i]:
    #             largest_prime = lst[i]
    #     i += 1

    # if largest_prime == 0:
    #     return 0

    # while largest_prime > 0:
    #     sum_of_digits += largest_prime % 10
    #     largest_prime //= 10

    # return sum_of_digits

    def is_prime(n: int) -> bool:
        """Check if integer is prime."""
        if n < 2:
            return False

        if n % 2 == 0 and n != 2:
            return False

        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False

        return True

    largest_prime = max(lst, default=0)
    sum_of_digits = sum(int(d) for d in str(largest_prime))

    return sum_of_digits
