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

    # --------------------------------------------------------------------------
    # Here's an implementation that uses two loops to find the answer:
    #
    #   even_count = 0
    #   odd_count = 0
    #   for i in range(1, n + 1):
    #       if str(i) == str(i)[::-1] and i % 2 == 0:
    #           even_count += 1
    #       elif str(i) == str(i)[::-1] and i % 2 == 1:
    #           odd_count += 1
    #   return even_count, odd_count
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Here's another implementation that uses a single loop with a tuple
    # unpacking to find the answer:
    #
    #   even_count = 0
    #   odd_count = 0
    #   for i in range(1, n + 1):
    #       if str(i) == str(i)[::-1]:
    #           if i % 2 == 0:
    #               even_count += 1
    #           else:
    #               odd_count += 1
    #   return even_count, odd_count
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Finally, we've provided an implementation using a single line of code
    # that utilizes a comprehension and the zip function:
    #
    #   return tuple(sum(1 for i in range(1, n + 1) if str(i) == str(i)[::-1] and i % 2 == j) for j in range(2))
    # --------------------------------------------------------------------------
    return tuple(sum(1 for i in range(1, n + 1) if str(i) == str(i)[::-1] and i % 2 == j) for j in range(2))
