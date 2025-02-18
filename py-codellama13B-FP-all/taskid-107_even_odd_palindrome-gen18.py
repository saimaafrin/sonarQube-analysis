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


    # Initialize variables
    even_count: int = 0
    odd_count: int = 0

    # Loop through each number from 1 to n
    for i in range(1, n + 1):
        # Get the reversed number
        reversed_num: int = reverse_num(i)

        # Check if the reversed number is equal to the original number
        if i == reversed_num:
            # If the original number is even, increment the even counter
            if is_even(i):
                even_count += 1
            # If the original number is odd, increment the odd counter
            else:
                odd_count += 1

    # Return the number of even and odd palindromes
    return even_count, odd_count
