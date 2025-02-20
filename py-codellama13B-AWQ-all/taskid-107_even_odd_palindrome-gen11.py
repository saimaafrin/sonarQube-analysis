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

    # Initialize number of even palindromes
    even_count = 0

    # Initialize number of odd palindromes
    odd_count = 0

    # Iterate over all integers in range(1, n)
    for i in range(1, n+1):
        # Get the reverse of i
        reverse = i[::-1]

        # Check if i is a palindrome
        if str(i) == str(reverse):
            # Check if i is even
            if i % 2 == 0:
                # Increment the count of even palindromes
                even_count += 1
            else:
                # Increment the count of odd palindromes
                odd_count += 1

    # Return the tuple of even and odd palindrome counts
    return (even_count, odd_count)
