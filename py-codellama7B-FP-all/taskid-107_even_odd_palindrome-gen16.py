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


    # Edge cases.
    if n <= 1:
        return 0, 0

    # Initialize the number of even and odd integer palindromes.
    num_even_palindromes = 0
    num_odd_palindromes = 0

    # Check for each integer palindrome in the range(1, n), inclusive.
    for i in range(1, n+1):
        # Skip odd numbers, since they are not palindromes.
        if i % 2 != 0:
            continue

        # Check if the number is a palindrome.
        if str(i) == str(i)[::-1]:
            # Even numbers are palindromes.
            if i % 2 == 0:
                num_even_palindromes += 1
            # Odd numbers are palindromes.
            else:
                num_odd_palindromes += 1

    return num_even_palindromes, num_odd_palindromes
