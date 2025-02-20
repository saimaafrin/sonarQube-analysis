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

    # Initialize counters for even and odd palindromes
    even_count, odd_count = 0, 0
    # Iterate over numbers from 1 to n
    for num in range(1, n+1):
        # Check if the number is a palindrome
        if str(num) == str(num)[::-1]:
            # If the number is a palindrome, check if it is even or odd
            if num % 2 == 0:
                # If the number is even, increment the even counter
                even_count += 1
            else:
                # If the number is odd, increment the odd counter
                odd_count += 1
    # Return a tuple of the counts
    return even_count, odd_count
