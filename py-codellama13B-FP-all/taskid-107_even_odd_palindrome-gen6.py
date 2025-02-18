from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

    >>> even_odd_palindrome(3)
    (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

    >>> even_odd_palindrome(12)
    (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """

    def is_palindrome(num: int) -> bool:
        return num == num[::-1]

    def is_even(num: int) -> bool:
        return num % 2 == 0

    def is_odd(num: int) -> bool:
        return num % 2 == 1

    even = 0
    odd = 0
    for num in range(1, n):
        if is_palindrome(num):
            if is_even(num):
                even += 1
            elif is_odd(num):
                odd += 1
    return even, odd
