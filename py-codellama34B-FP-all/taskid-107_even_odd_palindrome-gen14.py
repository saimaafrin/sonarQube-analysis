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

    # edge case
    if n == 1: return 1, 0
    if n == 2: return 0, 2

    # n >= 3
    even_cnt, odd_cnt = 1, 2
    for i in range(3, n+1):
        # first, i is odd
        if i % 2 == 1:
            odd_cnt += 1
        else:
            # if i is even, then i must be even palindrome
            even_cnt += 1
        # second, i is even
        if i % 2 == 0:
            even_cnt += 1
        else:
            # if i is odd, then i must be odd palindrome
            odd_cnt += 1

    return even_cnt, odd_cnt
