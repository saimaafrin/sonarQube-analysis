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


    def _is_palindrome(n: int) -> bool:
        return str(n) == str(n)[::-1]

    def _is_even(n: int) -> bool:
        return n % 2 == 0

    def _range(n: int) -> int:
        return n * 2 + 1

    even, odd = 0, 0

    for i in range(_range(n)):
        if _is_palindrome(i) and _is_even(i):
            even += 1
        elif _is_palindrome(i) and _is_odd(i):
            odd += 1

    return even, odd
