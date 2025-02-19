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


    def _is_palindrome(num):
        """Check if a given integer is palindrome"""
        return str(num) == str(num)[::-1]

    def _count_even_palindromes(num):
        """Count number of even palindrome"""
        count = 0
        for i in range(10, num + 1):
            if _is_palindrome(i):
                count += 1
        return count

    def _count_odd_palindromes(num):
        """Count number of odd palindrome"""
        count = 0
        for i in range(11, num + 1, 2):
            if _is_palindrome(i):
                count += 1
        return count

    return (_count_even_palindromes(n), _count_odd_palindromes(n))
