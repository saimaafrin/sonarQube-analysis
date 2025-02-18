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

    # Initialize the count of even and odd palindromes
    count_even, count_odd = 0, 0

    # Iterate over all the numbers between 1 and n
    for i in range(1, n + 1):
        # If i is a palindrome
        if str(i) == str(i)[::-1]:
            # Increment the counter for even or odd palindromes
            if i % 2 == 0:
                count_even += 1
            else:
                count_odd += 1

    # Return the final count of even and odd palindromes
    return count_even, count_odd
