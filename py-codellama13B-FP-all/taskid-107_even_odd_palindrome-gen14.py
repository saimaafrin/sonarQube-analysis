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


    # Initialize the result tuple with (0, 0)
    result: Tuple[int, int] = (0, 0)

    # Iterate from 1 to n and check if each number is a palindrome.
    for number in range(1, n + 1):

        # Check if the number is a palindrome
        if str(number) == str(number)[::-1]:

            # Update the result tuple accordingly.
            if number % 2 == 0:
                result = (result[0] + 1, result[1])
            else:
                result = (result[0], result[1] + 1)

    # Return the result
    return result
