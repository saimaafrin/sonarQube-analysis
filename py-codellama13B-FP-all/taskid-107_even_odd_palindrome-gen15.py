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

    count = [0, 0]
    # time O(n) and space O(1)
    for i in range(1, n + 1):
        rev = 0
        ori = i
        while i > 0:
            rev = rev * 10 + i % 10
            i = i // 10
        if ori == rev:
            count[1] += 1 if i % 2 == 0 else 0
            count[0] += 1 if i % 2 == 1 else 0
    return count[0], count[1]
