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
        Given a positive integer, check if it is palindrome or not.
        """
        return str(n) == str(n)[::-1]
    
    even_palindrome_count = 0
    odd_palindrome_count = 0
    
    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_palindrome_count += 1
            else:
                odd_palindrome_count += 1
    
    return even_palindrome_count, odd_palindrome_count
