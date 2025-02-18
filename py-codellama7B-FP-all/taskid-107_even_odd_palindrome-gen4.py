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


    def is_palindrome(n: int) -> bool:
        """
        Check whether an integer is a palindrome.

        Args:
            n: A non-negative integer.

        Return:
            True if n is a palindrome, otherwise False.
        """
        return str(n) == str(n)[::-1]

    def is_even_palindrome(n: int) -> bool:
        """
        Check whether an integer is an even palindrome.

        Args:
            n: A non-negative integer.

        Return:
            True if n is an even palindrome, otherwise False.
        """
        return is_palindrome(n) and n % 2 == 0

    def is_odd_palindrome(n: int) -> bool:
        """
        Check whether an integer is an odd palindrome.

        Args:
            n: A non-negative integer.

        Return:
            True if n is an odd palindrome, otherwise False.
        """
        return is_palindrome(n) and n % 2 == 1

    even_palindromes, odd_palindromes = 0, 0
    for i in range(1, n + 1):
        if is_even_palindrome(i):
            even_palindromes += 1
        elif is_odd_palindrome(i):
            odd_palindromes += 1

    return even_palindromes, odd_palindromes
