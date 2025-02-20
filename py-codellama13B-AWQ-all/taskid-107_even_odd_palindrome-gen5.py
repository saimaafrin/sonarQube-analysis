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

    # Initialize the variables
    count_even, count_odd = 0, 0

    # Iterate over the range of numbers
    for i in range(1, n+1):
        # Get the string representation
        s = str(i)
        # Check if the string is a palindrome
        if s == s[::-1]:
            # Check if the string has an even length
            if len(s) % 2 == 0:
                # Increment the count of even palindromes
                count_even += 1
            else:
                # Increment the count of odd palindromes
                count_odd += 1

    # Return the count of even and odd integer palindromes
    return (count_even, count_odd)
