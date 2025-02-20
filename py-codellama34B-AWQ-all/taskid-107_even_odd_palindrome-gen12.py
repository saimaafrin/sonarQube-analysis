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
    odd_count = 0
    even_count = 0

    # Iterate from 1 to n
    for num in range(1, n+1):
        # Convert num to string
        num_str = str(num)

        # Check if num_str is palindrome
        if num_str == num_str[::-1]:
            # If num is even, increment even_count
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    # Return tuple with even_count and odd_count
    return even_count, odd_count
